# Petri-net-marking-tree
A python script that displays the marking tree for a given Petri net





How to create a Petri net:

1 - Creating a place: p1 = Place("p1", 3) where "p1" is its name and 3 are its tokens.	

2 - Creating an arc: a1 = Arc(3) where 3 is its cost(the cost is 1 per default).

3 - Creating a transition: t4 = Transition("t4", [a8, a9], [a1]) where "t4" is its name,
[a8, a9] are the input arcs and [a1] is the output arc.

4 - Now assign the start and end nodes(place or transition) to the arcs: 
a8.assign_start_end(p3, t4) (p3 is the start node and t4 is the end node).

5 - Creating a Petri net: petri = PetriNet([t1, t2, t3, t4]) 
where [t1, t2, t3, t4] are the Petri net transitions.
<br/><br/><br/><br/><br/>
The marking tree display:

display the Petri net's marking tree with: petri.marking_tree(petri.get_marking()) 
where petri is a PetriNet object.



A Petri net marking tree display example:

In this example(example 1):

the marking M1 is the child of M0 passing by the transition t5

the markings M2 and M0 are the children of M1 passing by the transitions t1 and t4 respectively

the markings M3 and M0 are the children of M2 passing by the transitions t2 and t3 respectively

![alt text](https://raw.githubusercontent.com/Badredine-Kheddaoui/Petri-net-marking-tree/master/Petri%20net%20marking%20tree%20display%20example.PNG)
	
	
