class Symbol(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def evaluate(self, scope):
        return scope.get(self.name)
