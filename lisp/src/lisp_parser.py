from collections import defaultdict
import re


class TreeNode(object):
    def __init__(self, text, offset, elements=None):
        self.text = text
        self.offset = offset
        self.elements = elements or []

    def __iter__(self):
        for el in self.elements:
            yield el


class TreeNode1(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode1, self).__init__(text, offset, elements)
        self.expression = elements[1]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self.expression = elements[0]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    REGEX_1 = re.compile('^[1-9]')
    REGEX_2 = re.compile('^[0-9]')
    REGEX_3 = re.compile('^[0-9]')
    REGEX_4 = re.compile('^[ \\n\\r\\t]')

    def _read_program(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['program'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 0, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_cell()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = self._actions.make_program(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['program'][index0] = (address0, self._offset)
        return address0

    def _read_cell(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['cell'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 0, self._offset, [], True
        while address2 is not FAILURE:
            address2 = self._read__()
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address3 = FAILURE
            address3 = self._read_expression()
            if address3 is not FAILURE:
                elements0.append(address3)
                address4 = FAILURE
                remaining1, index3, elements2, address5 = 0, self._offset, [], True
                while address5 is not FAILURE:
                    address5 = self._read__()
                    if address5 is not FAILURE:
                        elements2.append(address5)
                        remaining1 -= 1
                if remaining1 <= 0:
                    address4 = TreeNode(self._input[index3:self._offset], index3, elements2)
                    self._offset = self._offset
                else:
                    address4 = FAILURE
                if address4 is not FAILURE:
                    elements0.append(address4)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.make_cell(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['cell'][index0] = (address0, self._offset)
        return address0

    def _read_expression(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['expression'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_list()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_atom()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['expression'][index0] = (address0, self._offset)
        return address0

    def _read_atom(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['atom'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        index2 = self._offset
        address1 = self._read_boolean()
        if address1 is FAILURE:
            self._offset = index2
            address1 = self._read_number()
            if address1 is FAILURE:
                self._offset = index2
                address1 = self._read_symbol()
                if address1 is FAILURE:
                    self._offset = index2
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            index3 = self._offset
            index4, elements1 = self._offset, []
            address3 = FAILURE
            index5 = self._offset
            address3 = self._read_delimiter()
            self._offset = index5
            if address3 is FAILURE:
                address3 = TreeNode(self._input[self._offset:self._offset], self._offset)
                self._offset = self._offset
            else:
                address3 = FAILURE
            if address3 is not FAILURE:
                elements1.append(address3)
                address4 = FAILURE
                if self._offset < self._input_size:
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('<any char>')
                if address4 is not FAILURE:
                    elements1.append(address4)
                else:
                    elements1 = None
                    self._offset = index4
            else:
                elements1 = None
                self._offset = index4
            if elements1 is None:
                address2 = FAILURE
            else:
                address2 = TreeNode(self._input[index4:self._offset], index4, elements1)
                self._offset = self._offset
            self._offset = index3
            if address2 is FAILURE:
                address2 = TreeNode(self._input[self._offset:self._offset], self._offset)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.make_atom(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['atom'][index0] = (address0, self._offset)
        return address0

    def _read_list(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['list'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '(':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"("')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                address3 = self._read_cell()
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address4 = FAILURE
                chunk1 = None
                if self._offset < self._input_size:
                    chunk1 = self._input[self._offset:self._offset + 1]
                if chunk1 == ')':
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('")"')
                if address4 is not FAILURE:
                    elements0.append(address4)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.make_list(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['list'][index0] = (address0, self._offset)
        return address0

    def _read_boolean(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['boolean'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 2]
        if chunk0 == '#t':
            address0 = self._actions.make_true(self._input, self._offset, self._offset + 2)
            self._offset = self._offset + 2
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"#t"')
        if address0 is FAILURE:
            self._offset = index1
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 2]
            if chunk1 == '#f':
                address0 = self._actions.make_false(self._input, self._offset, self._offset + 2)
                self._offset = self._offset + 2
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"#f"')
            if address0 is FAILURE:
                self._offset = index1
        self._cache['boolean'][index0] = (address0, self._offset)
        return address0

    def _read_number(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['number'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        index2 = self._offset
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '-':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"-"')
        if address1 is FAILURE:
            address1 = TreeNode(self._input[index2:index2], index2)
            self._offset = index2
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            index3 = self._offset
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 == '0':
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"0"')
            if address2 is FAILURE:
                self._offset = index3
                index4, elements1 = self._offset, []
                address3 = FAILURE
                chunk2 = None
                if self._offset < self._input_size:
                    chunk2 = self._input[self._offset:self._offset + 1]
                if chunk2 is not None and Grammar.REGEX_1.search(chunk2):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[1-9]')
                if address3 is not FAILURE:
                    elements1.append(address3)
                    address4 = FAILURE
                    remaining0, index5, elements2, address5 = 0, self._offset, [], True
                    while address5 is not FAILURE:
                        chunk3 = None
                        if self._offset < self._input_size:
                            chunk3 = self._input[self._offset:self._offset + 1]
                        if chunk3 is not None and Grammar.REGEX_2.search(chunk3):
                            address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                            self._offset = self._offset + 1
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('[0-9]')
                        if address5 is not FAILURE:
                            elements2.append(address5)
                            remaining0 -= 1
                    if remaining0 <= 0:
                        address4 = TreeNode(self._input[index5:self._offset], index5, elements2)
                        self._offset = self._offset
                    else:
                        address4 = FAILURE
                    if address4 is not FAILURE:
                        elements1.append(address4)
                    else:
                        elements1 = None
                        self._offset = index4
                else:
                    elements1 = None
                    self._offset = index4
                if elements1 is None:
                    address2 = FAILURE
                else:
                    address2 = TreeNode(self._input[index4:self._offset], index4, elements1)
                    self._offset = self._offset
                if address2 is FAILURE:
                    self._offset = index3
            if address2 is not FAILURE:
                elements0.append(address2)
                address6 = FAILURE
                index6 = self._offset
                index7, elements3 = self._offset, []
                address7 = FAILURE
                chunk4 = None
                if self._offset < self._input_size:
                    chunk4 = self._input[self._offset:self._offset + 1]
                if chunk4 == '.':
                    address7 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address7 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"."')
                if address7 is not FAILURE:
                    elements3.append(address7)
                    address8 = FAILURE
                    remaining1, index8, elements4, address9 = 1, self._offset, [], True
                    while address9 is not FAILURE:
                        chunk5 = None
                        if self._offset < self._input_size:
                            chunk5 = self._input[self._offset:self._offset + 1]
                        if chunk5 is not None and Grammar.REGEX_3.search(chunk5):
                            address9 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                            self._offset = self._offset + 1
                        else:
                            address9 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('[0-9]')
                        if address9 is not FAILURE:
                            elements4.append(address9)
                            remaining1 -= 1
                    if remaining1 <= 0:
                        address8 = TreeNode(self._input[index8:self._offset], index8, elements4)
                        self._offset = self._offset
                    else:
                        address8 = FAILURE
                    if address8 is not FAILURE:
                        elements3.append(address8)
                    else:
                        elements3 = None
                        self._offset = index7
                else:
                    elements3 = None
                    self._offset = index7
                if elements3 is None:
                    address6 = FAILURE
                else:
                    address6 = TreeNode(self._input[index7:self._offset], index7, elements3)
                    self._offset = self._offset
                if address6 is FAILURE:
                    address6 = TreeNode(self._input[index6:index6], index6)
                    self._offset = index6
                if address6 is not FAILURE:
                    elements0.append(address6)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.make_number(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['number'][index0] = (address0, self._offset)
        return address0

    def _read_symbol(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['symbol'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_symbol_char()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = self._actions.make_symbol(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['symbol'][index0] = (address0, self._offset)
        return address0

    def _read_symbol_char(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['symbol_char'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        index2 = self._offset
        address1 = self._read_delimiter()
        self._offset = index2
        if address1 is FAILURE:
            address1 = TreeNode(self._input[self._offset:self._offset], self._offset)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            if self._offset < self._input_size:
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('<any char>')
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['symbol_char'][index0] = (address0, self._offset)
        return address0

    def _read_delimiter(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['delimiter'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '#':
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"#"')
        if address0 is FAILURE:
            self._offset = index1
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 == '(':
                address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"("')
            if address0 is FAILURE:
                self._offset = index1
                chunk2 = None
                if self._offset < self._input_size:
                    chunk2 = self._input[self._offset:self._offset + 1]
                if chunk2 == ')':
                    address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('")"')
                if address0 is FAILURE:
                    self._offset = index1
                    address0 = self._read__()
                    if address0 is FAILURE:
                        self._offset = index1
        self._cache['delimiter'][index0] = (address0, self._offset)
        return address0

    def _read__(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['_'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 is not None and Grammar.REGEX_4.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[ \\n\\r\\t]')
        self._cache['_'][index0] = (address0, self._offset)
        return address0


class Parser(Grammar):
    def __init__(self, input, actions, types):
        self._input = input
        self._input_size = len(input)
        self._actions = actions
        self._types = types
        self._offset = 0
        self._cache = defaultdict(dict)
        self._failure = 0
        self._expected = []

    def parse(self):
        tree = self._read_program()
        if tree is not FAILURE and self._offset == self._input_size:
            return tree
        if not self._expected:
            self._failure = self._offset
            self._expected.append('<EOF>')
        raise ParseError(format_error(self._input, self._failure, self._expected))


def format_error(input, offset, expected):
    lines, line_no, position = input.split('\n'), 0, 0
    while position <= offset:
        position += len(lines[line_no]) + 1
        line_no += 1
    message, line = 'Line ' + str(line_no) + ': expected ' + ', '.join(expected) + '\n', lines[line_no - 1]
    message += line + '\n'
    position -= len(line) + 1
    message += ' ' * (offset - position)
    return message + '^'

def parse(input, actions=None, types=None):
    parser = Parser(input, actions, types)
    return parser.parse()
