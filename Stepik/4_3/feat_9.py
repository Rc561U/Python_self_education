class StringDigit(str):

	def __init__(self,string):
		self.__check_value(string)
		self.st_int = string	
		

	@staticmethod
	def __check_value(val):
		try:
			val = int(val)
		except:
			raise ValueError("в строке должны быть только цифры")

	def __radd__(self,value):
		self.__check_value(value)
		return StringDigit(value + self.st_int)

	def __add__(self,value):
		self.__check_value(value)
		return StringDigit(self.st_int + value)


sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
print(sd)
sd = "789" + sd # StringDigit: 789123456
print(sd)
