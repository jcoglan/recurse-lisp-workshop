class Bool(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        if self.value:
            return '#t'
        else:
            return '#f'

    def evaluate(self, scope):
        if self.value == True:
        	return True
        elif self.value == False:
        	return False
        return
