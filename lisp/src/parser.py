import lisp_parser
from nodes import Symbol, Int, Float, Bool, List, Program


def parse(program):
    return lisp_parser.parse(program, actions=Actions())


class Actions(object):
    def make_symbol(self, input, start, end, elements):
        return Symbol(input[start:end])

    def make_atom(self, input, start, end, elements):
        return elements[0]

    def make_cell(self, input, start, end, elements):
        return elements[1]

    def make_number(self, input, start, end, elements):
        text = input[start:end]
        if elements[2].text == '':
            return Int(int(text))
        else:
            return Float(float(text))

    def make_true(self, input, start, end):
        return Bool(True)

    def make_false(self, input, start, end):
        return Bool(False)

    def make_list(self, input, start, end, elements):
        return List.from_array(elements[1].elements)

    def make_program(self, input, start, end, elements):
        return Program(elements)
