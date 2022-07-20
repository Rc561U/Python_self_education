class Bag:
	def __init__(self,max_weight):
		self.max_weight = max_weight
		self.__things = []
		self.__weight = 0

	def __check_weight(self,new_t,old_t=None):
		w = self.__weight + new_t.weight if old_t is None else self.__weight + new_t.weight - old_t.weight
		if w > self.max_weight:
			raise ValueError('превышен суммарный вес предметов')

	def __check_index(self,index):
		if not (0 <= index < len(self.__things)):
			raise IndexError('неверный индекс')

	def add_thing(self,thing):
		self.__check_weight(thing)
		self.__things.append(thing)
		self.__weight += thing.weight

	def __getitem__(self,item):
		self.__check_index(item)
		return self.__things[item]

	def __setitem__(self,key,value):
		self.__check_index(key)
		t = self.__things[key]
		self.__check_weight(value,t)
		self.__things[key] = value
		self.__weight += (value.weight-t.weight)

	def __delitem__(self,key):
		self.__check_index(key)
		t = self.__things.pop(key)
		self.__weight -=t.weight
		
class Thing:
	def __init__(self,name,weight):
		self.name = name
		self.weight = weight



bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок