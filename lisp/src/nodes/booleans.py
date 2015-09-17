class Bool(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        if self.value:
            return '#t'
        else:
            return '#f'

    def evaluate(self, env):
        pass
