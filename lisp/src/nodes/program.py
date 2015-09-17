class Program(object):
    def __init__(self, expressions):
        self.expressions = expressions

    def __repr__(self):
        return '\n'.join([x.__repr__() for x in self.expressions])

    def evaluate(self, env):
        pass
