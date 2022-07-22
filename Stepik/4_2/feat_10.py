class IteratorAttrs:
	def __iter__(self):
		for i in self.__dict__.items():
			yield i

class SmartPhone(IteratorAttrs):
	def __init__(self,model,size,memory):
		self.model = model
		self.size = size
		self.memory = memory