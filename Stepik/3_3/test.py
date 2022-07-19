class WordString:


	def __init__(self,st=""):
		self.__st = st
		self.__index = None

	def __call__(self, string):
		if isinstance(string,int):
			return self.__st[string]
		self.__st = string

	def __len__(self):
		return len(self.__st)

	@property
	def string(self):
		return ' '.join(self.__st)

	@string.setter
	def string(self,value):
		self.__st = value.split()


words = WordString()
words.string = "Курс по Python ООП"
print(len(words))
print(words.string)
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)