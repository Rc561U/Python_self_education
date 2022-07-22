class Thing:
	def __init__(self,name,weight):
		self.name = name
		self.weight = weight

class ArtObject(Thing):
	def __init__(self,name,weight,author,date):
		super().__init__(name,weight)
		self.author = author
		self.date = date

class Computer(Thing):
	def __init__(self,name,weight,memory,cpu):
		super().__init__(name,weight)
		self.memory = memory
		self.cpu = cpu


class Auto(Thing):
	def __init__(self,name,weight,dims,model=None):
		super().__init__(name,weight)
		self.dims = dims
		self.model = model

class Mercedes(Auto):
	def __init__(self,name, weight, dims,model,old):
		super().__init__(name, weight, dims,model)
		self.old = old


class Toyota(Auto):
	def __init__(self,name, weight, dims,model,wheel):
		super().__init__(name, weight, dims,model)
		self.wheel = wheel
		

obj1 = ArtObject('name', 100.45, 'author', 'date')
auto1 = Mercedes('name', 100004.6, (1.2, 2.3, 3.4), 'model', 10) 