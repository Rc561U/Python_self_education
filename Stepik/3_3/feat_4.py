class WordString:


	def __init__(self,string=""):
		self.strin = string.split()

	def __len__(self,words):
		return len(self.words)


	# def __call__(self,*args,**kwargs):


	def words(self, indx):
		return self.strin[indx]


	@property
	def string(self):
		return self.strin

	@string.setter
	def string(self,value):
		self.strin = value

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")