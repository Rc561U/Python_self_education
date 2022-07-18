class WordString:
	def __init__(self,st):
		self.st = st


	def __call__(self,string,*args,**kwargs):
		return "That's work"

	def __str__(self):
		return self.st
words = WordString("Курс по Python ООП")
print(words)