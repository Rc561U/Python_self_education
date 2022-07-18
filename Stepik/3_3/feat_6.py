class Complex:
	def __init__(self,real,img):
		self.__real = self.__img = 0
		self.real = real
		self.img = img

	@property
	def real(self):
		return self.__real

	@real.setter
	def real(self, value):
		if type(value) not in (int,float):
			raise ValueError("Неверный тип данных.")
		self.__real = value

	@property
	def img(self):
		return self.__img

	@img.setter
	def img(self, value):
		if type(value) not in (int,float):
			raise ValueError("Неверный тип данных.")
		self.__img = value

	def __abs__(self):
		return (self.__real * self.__real + self.__img * self.__img)**0.5

cmp = Complex(7,8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)