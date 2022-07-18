import itertools


class FloatValue:

	def __set_name__(self,owner,name):
		self.name = "_" + name

	def __get__(self,instance,owner):
		return getattr(instance,self.name)
	def __set__(self,instance,value):
		if isinstance(value, float):
			setattr(instance, self.name, value)
		else:
			raise TypeError("Присваивать можно только вещественный тип данных.")


class Cell:
	value = FloatValue()

	def __init__(self,value=0.0):
		self.value = value

class TableSheet:

	def __init__(self, N, M):
		
		counter = itertools.count(1.0)
		self.cells = [[Cell(next(counter)) for x in range(N)] for i in range(M)]

table = TableSheet(5,3)


