class Singleton:
	__instance = None

	def __new__(cls,*args,**kwargs):
		if Singleton.__instance is None:
			Singleton.__instance = super().__new__(cls)
		return Singleton.__instance



class Game(Singleton):
	def __init__(self,name):
		if 'name' not in self.__dict__:
			self.name = name