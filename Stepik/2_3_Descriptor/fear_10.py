class TVProgram:
	def __init__(self,name):
		self.name = name

		self.items = []

	def add_telecast(self,tl):
		self.items.append(tl)

	def remove_telecast(self,indx):
		tl_lst = tuple(filter(lambda x: x.uid == indx, self.items))
		for t in tl_lst:
			self.items.remove(t)

class Telecast:

	def __init__(self,id,name,dur):

		self.__id = id
		self.__name = name
		self.__duration = dur

	@property
	def uid(self):
		return self.__id
	@uid.setter
	def uid(self,value):
		self.__id = value


	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,value):
		self.__name = value


	@property
	def duration(self):
		return self.__duration
	@duration.setter
	def duration(self,value):
		self.__duration = value
		

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")