class Integer:
	def __init__(self,start_value=0):
		self.__value = start_value
		


	@property
	def value(self):
		return self.__value

	@value.setter
	def value(self,value):
		if type(value) != int:
			raise ValueError('должно быть целое число')
		self.__value = value

	def __repr__(self):
		return str(self.__value)




class Array:
	def __init__(self,max_lenght,cell):
		self.__max_lenght = max_lenght
		self.__cell = cell
		self.__array = [self.__cell() for _ in range(self.__max_lenght)]

	def __check(self,inx):
		if not isinstance(inx,int) or not (-self.__max_lenght <= inx < self.__max_lenght):
			raise IndexError('неверный индекс для доступа к элементам массива')

	def __getitem__(self,item):
		self.__check(item)
		return self.__array[item].value

	def __setitem__(self,key,value):
		self.__check(key)
		self.__array[key].value = value

	def __repr__(self):
		return " ".join(map(str,self.__array))



ar_int = Array(10, cell=Integer)
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[8] = 10
ar_int[1] = 10

print(ar_int)