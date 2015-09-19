class List(object):
    @classmethod
    def from_array(cls, elements):
        if elements:
            return cls(elements[0], cls.from_array(elements[1:]))
        else:
            return NULL

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        list = []
        node = self
        while node != NULL:
            list.append(node.head)
            node = node.tail
        return '(' + ' '.join([repr(x) for x in list]) + ')'

    def evaluate(self, scope):
        print "list head: " + repr(self.head)
        print "list tail: " + repr(self.tail)

        if self.head.name == 'define':
            scope.set(self.tail.head.name, self.tail.tail.head.evaluate(scope))

        elif self.head.name == 'if':
            pass  # todo

        else:
            fun = scope.get(self.head.name)
            return [fun.evaluate(*self.tail)]



NULL = List()
