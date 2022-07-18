class SuperShop:

	def __init__(self,title):
		self.name = title
		self.goods = list()

	def add_product(self,product):
		self.goods.append(product)

	def remove_product(self,product):
		self.goods.remove(product)

class StringValue:

	def __init__(self,min=2,max=50):
		self.min = min
		self.max = max

	def __set_name__(self,owner,name):
		self.name = "_" + name

	def __get__(self,instance,owner):
		return getattr(instance, self.name)

	def __set__(self,instance,value):
		if isinstance(value, str) and self.min <= len(value) <= self.max:
			setattr(instance, self.name, value)

class PriceValue:

	def __init__(self,max_val):
		self.max = max_val
	
	def __set_name__(self,owner,name):
		self.name = "_" + name

	def __get__(self,instance,owner):
		return getattr(instance, self.name)

	def __set__(self,instance,value):
		if isinstance(value, (float,int)) and 0 <= value <= self.max:
			setattr(instance,self.name,value)
			

class Product:
	name = StringValue(2,50) 
	price = PriceValue(10000)

	def __init__(self,name,price):
		self.name = name
		self.price = price

shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")