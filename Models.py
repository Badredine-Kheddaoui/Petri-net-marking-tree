class Place:
    def __init__(self, name, tokens):
        self.name = name
        self.tokens = tokens

    def __repr__(self):
        return str(self.tokens)


class Transition:
    def __init__(self, name, input_arcs, output_arcs):
        self.name = name
        self.input_arcs = input_arcs
        self.output_arcs = output_arcs

    # check if the transition is executable
    def is_executable(self):
        for i in self.input_arcs:
            if i.start.tokens < i.cost:
                return False
        return True

    # execute the transition
    def execute(self):
        for i in self.input_arcs:
            if i.start.tokens < i.cost:
                return False
        for i in self.input_arcs:
            i.start.tokens -= i.cost
        for o in self.output_arcs:
            o.end.tokens += o.cost
        return True

    def __repr__(self):
        string = f'{self.name}:\ninput_arcs: ('
        for i in self.input_arcs:
            string += i.name + ', '
        string = string[:len(string) - 2] + ')'

        string += '\noutput_arcs: ('
        for i in self.output_arcs:
            string += i.name + ', '
        string = string[:len(string) - 2] + ')'

        return string


class Arc:
    def __init__(self, cost=1):
        self.cost = cost
        self.start = None
        self.end = None

    def assign_start_end(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'starts at {type(self.start).__name__.lower()} {self.start.name} ' \
            f'and ends at {type(self.end).__name__.lower()} {self.end.name} ' \
            f'and costs {self.cost}'


class Marking:
    def __init__(self, places):
        self.places = places

    def __eq__(self, other):
        # print(f'comparing: {self} with  {other}')
        if isinstance(other, Marking) and len(self.places) == len(other.places):
            for i in range(len(self.places)):
                if self.places[i] != other.places[i]:
                    return False
            return True
        return False

    def __repr__(self):
        string = '('
        for p in self.places:
            string += f'{p}, '
        return string[:len(string)-2] + ')'
