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
        return '(' + ' '.join([x.__repr__() for x in list]) + ')'

    def evaluate(self, env):
        pass


NULL = List()
