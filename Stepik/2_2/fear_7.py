class RadiusVector2D:
	MIN_COORD = -100
	MAX_COORD = 1024
	def __init__(self,x=0,y=0):
		self.__x=0
		self.__y=0
		self.x = x
		self.y = y

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self,newx):
		if self.__vector_checker(newx):
			self.__x = newx

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self,newy):
		if self.__vector_checker(newy):
			self.__y = newy

	@classmethod
	def __vector_checker(cls,value):
		return type(value) in (int,float) and cls.MIN_COORD <= value <= cls.MAX_COORD
		

	@staticmethod
	def norm2(vector):
		x = vector.x
		y = vector.y
		return x*x + y*y