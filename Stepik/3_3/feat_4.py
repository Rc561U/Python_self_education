class WordString:


	def __init__(self,st=None):
		self.__str = st[:] if st and type(st) == str else [] 

	def __len__(self):
		return len(self.__strin)


	

	def __call__(self,string,*args,**kwargs):
		if isinstance(string,int):
			return self.__strin[string]
		self.__strin = string


	@property
	def string(self):
		return self.__strin#' '.join(self.__strin)

	@string.setter
	def string(self,value):
		self.__strin = value.split()

words = WordString()
words.string = "k"
n = len(words)
print(n)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")