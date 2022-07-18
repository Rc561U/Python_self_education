class Integer:
	@classmethod
	def verify_coord(cls, coord):
		if type(coord) != int:
			raise TypeError('Coordinate have to be a integer!')

	def __set_name__(self, owner, name):
		self.name = "_" + name

	def __get__(set,instance,owner):
		return getattr(instance, self.name) 

	def __set__(self,instance,value):
		self.verify_coord(value)
		setattr(instance,self.name, value)


class Point3D:
	x = Integer()
	y = Integer()
	z = Integer()

	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z

	

p = Point3D(1,2,3)			
print(p.__dict__)

class RealValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Point:
    x = RealValue()
    y = RealValue()

    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1.5, 2.3)
pt.__dict__['x'] = 10.0
print(pt.x,pt.__dict__)


