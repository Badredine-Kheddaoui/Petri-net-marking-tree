#!/usr/bin/env python3
import copy

from Models import *


class PetriNet:
    # markings that have been found
    markings = list()
    # these two variables are used to make the display look better
    mark_numbers = 0
    tabs = 0

    def __init__(self, transitions):
        self.transitions = transitions

    def __repr__(self):
        string = ''
        for t in self.transitions:
            string += f'{t}\n'
        return string

    '''
    displays the initial marking if it has not been found before 
    and also children markings that are already found before
    '''
    def marking_tree(self, initial_marking, tabs=0, transition=0):
        for i in range(len(self.transitions)):
            # if the initial marking has not been found yet, then add it to the markings list and print it
            if not self.already_exists(initial_marking):
                PetriNet.markings.append(initial_marking)
                for t in range(tabs):
                    print('\t', end='')
                if transition:
                    print(f'{transition}-->', end='')
                print(f'M{PetriNet.mark_numbers}', initial_marking)
                PetriNet.mark_numbers += 1

            # if a transition is executable then save this Petri Net, make a copy of it and execute the transition
            if self.transitions[i].is_executable():
                for t in range(tabs):
                    print('\t', end='')
                petri_copy = copy.deepcopy(self)
                petri_copy.transitions[i].execute()

                # if it gives a new marking then pass it the new marking_tree() call.
                if not self.already_exists(petri_copy.get_marking()):
                    PetriNet.tabs += 1
                    petri_copy.marking_tree(petri_copy.get_marking(), PetriNet.tabs, self.transitions[i].name)
                    PetriNet.tabs -= 1

                # if it's an old marking then just print it
                else:
                    for t in range(tabs + 1):
                        print('\t', end='')
                    print(f'{self.transitions[i].name}-->M{PetriNet.markings.index(petri_copy.get_marking())}',
                          petri_copy.get_marking())

    '''
    tests if a marking is already defined
    '''
    def already_exists(self, marking):
        for mark in PetriNet.markings:
            # print(f'comparing {mark} and {m}')
            if mark == marking:
                return True

    '''
    browse the all the net's places and get their tokens,
    returns a marking object
    '''
    def get_marking(self):
        places = list()
        for t in self.transitions:
            for i in t.input_arcs:
                if not places.__contains__(i.start):
                    places.append(i.start)
            for o in t.output_arcs:
                if not places.__contains__(o.end):
                    places.append(o.end)
        places = sorted(places, key=lambda x: x.name)
        places = self.places_to_ints(places)
        m = Marking(places)
        return m

    '''
    converts a list of places to a list of integers
    '''
    def places_to_ints(self, places):
        ints = list()
        for p in places:
            ints.append(p.tokens)
        return ints


def main():
    # a Place constructor assign a name and tokens to the place
    p1 = Place("p1", 3)
    p2 = Place("p2", 0)
    p3 = Place("p3", 0)

    # we cannot assign start and end points to arcs now because they could be transitions
    # and transitions themselves need arcs to be instantiated
    # an Arc constructor assign a cost to the arc(1 per default)
    a1 = Arc(3)
    a2 = Arc(2)
    a3 = Arc()
    a4 = Arc()
    a5 = Arc()
    a6 = Arc()
    a7 = Arc()
    a8 = Arc()
    a9 = Arc()

    # a Transition constructor assign a name and two lists of arcs as inputs and outputs to the transition
    t1 = Transition("t1", [a2], [a3])
    t2 = Transition("t2", [a4], [a5])
    t3 = Transition("t3", [a6], [a7])
    t4 = Transition("t4", [a8, a9], [a1])

    # now that the transitions are created we can assign start and end points to the arcs
    a1.assign_start_end(t4, p1)
    a2.assign_start_end(p1, t1)
    a3.assign_start_end(t1, p2)
    a4.assign_start_end(p2, t2)
    a5.assign_start_end(t2, p3)
    a6.assign_start_end(p3, t3)
    a7.assign_start_end(t3, p2)
    a8.assign_start_end(p3, t4)
    a9.assign_start_end(p1, t4)

    # the transitions contain arcs and arcs contain places so the transitions are all that is needed to initialize a Petri Net
    petri = PetriNet([t1, t2, t3, t4])

    petri.marking_tree(petri.get_marking())


if __name__ == '__main__': main()
