class Point:

	def __init__(self,x,y):
		self.__x = x
		self.__y = y

	def get_coords(self):
		return self.__x, self.__y


class Rectangle:

	def __init__(self,x1,y1,x2=None,y2=None):
		self.__sp = self.__ep = None
		if isinstance(x1, Point) and isinstance(y1, Point):
			self.__sp = x1
			self.__ep = y1
		elif all(map(lambda x: type(x) in (int,float),(x1,y1,x2,y2))):
				
			self.__sp = Point(x1,y1)
			self.__ep = Point(x2,y2)

	def set_coords(self, sp, ep):
		self.__sp = sp
		self.__ep = ep

	def get_coords(self):
		return self.__sp,self.__ep

	def draw(self):
		pone = self.__sp.get_coords()
		ptwo = self.__ep.get_coords()

		print(f"Прямоугольник с координатами: {pone} {ptwo}")

x1 = Point(0,0)
x2 = Point(20,34)
rect = Rectangle(x1,x2)
rect.draw()