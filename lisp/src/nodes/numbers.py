class Int(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def evaluate(self, scope):
        pass


class Float(Int):
    pass
