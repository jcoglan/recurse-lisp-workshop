class Function(object):
    def evaluate(self):
    	pass

class EqualsFunction(object):
	@classmethod
	def evaluate(self, *args):
		return all(args[0] == arg for arg in args)

class PlusFunction(object):
	@classmethod
	def evaluate(self, *args):
		return sum(args)

