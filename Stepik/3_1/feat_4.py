class Shop:


	def __init__(self,name):
		self.name = name
		self.goods = []

	def add_product(self,product):
		self.goods.append(product)

	def remove_product(self,product):
		self.goods.remove(product)

class Product:
	_id_instance = 1
	attr = {"name":(str,),"weight":(float,int),"price":(int,float)}
	def __init__(self,name,weight,price):
		self.id = id(self)
		# self.id = Product._id_instance
		# Product._id_instance +=1

		self.name = name
		self.weight = weight
		self.price = price

	def __setattr__(self,key,value):
		if key in self.attr and type(value) in self.attr[key]:
			if (key == 'price' or key == 'weight') and value <= 0:
				raise TypeError("Неверный тип присваиваемых данных.")
		elif key in self.attr:
				raise TypeError("Неверный тип присваиваемых данных.")
		super().__setattr__(key,value)

	def __delattr__(self,key):
		if key == 'id':
			raise AttributeError("Атрибут id удалять запрещено.")


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
