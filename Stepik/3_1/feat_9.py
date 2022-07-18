class Dimensions:
	MIN_DIMENSION = 10
	MAX_DIMENSION = 1000

	def __init__(self,a,b,c):
		self.__a = self.__b = self.__c = None
		self.a = a
		self.b = b
		self.c = c

	@property
	def a(self):
		return self.__a

	@a.setter
	def a(self,value):
		if self._verify_value(value):
			self.__a = value

	@property
	def b(self):
		return self.__b

	@b.setter
	def b(self,value):
		if self._verify_value(value):
			self.__b = value

	@property
	def c(self):
		return self.__c

	@c.setter
	def c(self,value):
		if self._verify_value(value):
			self.__c = value
	@classmethod
	def _verify_value(cls,value):
		return type(value) in (int,float) and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION
			

	def __setattr__(self,key,value):
		if key in ("MIN_DIMENSION", "MAX_DIMENSION"):
			raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

		super().__setattr__(key,value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10  # исключение AttributeError

class Property:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'
        self.min = owner.MIN_DIMENSION
        self.max = owner.MAX_DIMENSION

    def __get__(self, instance, owner):
        if instance:
            return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.min <= value <= self.max:
            setattr(instance, self.name, value)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = Property()
    b = Property()
    c = Property()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        object.__setattr__(self, key, value)


def type(arg):
    return property