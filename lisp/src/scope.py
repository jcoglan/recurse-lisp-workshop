from function import Function, PlusFunction, EqualsFunction

class Scope(object):
    def __init__(self):
        self.d = {}
        
    def set(self, key, value):
        self.d[key] = value

    def get(self, key):
        return self.d[key]


class TopLevel(Scope):
    def __init__(self):
        super(TopLevel, self).__init__()
        self.set('+', plus)
        self.set('=', equals)

plus = PlusFunction()
equals = EqualsFunction()
