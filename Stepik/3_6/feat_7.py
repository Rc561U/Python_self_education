class DataBase:
	def __init__(self,path):
		self.path = path
		self.dict_db = {}

	def write(self,record):
		self.dict_db.setdefault(record,[])
		self.dict_db[record].append(record)

	def read(self,pl):
		x = (x for row in self.dict_db(values) for x in row)		
		obj = tuple(filter(lambda x: x.pk == pl, x))
		return obj[0] if len(obj) > 0 else None


class Record:
	record_count = 0

	def __init__(self,fio,descr,old):
		self.fio = fio.lower()
		self.descr = descr
		self.old = old
		self.pk = self.__count()
   		
	@classmethod
	def __count(cls):
		cls.record_count += 1
		return cls.record_count


	def __hash__(self):
   		return hash((self.fio, self.old))

	def __eq__(self,other):
   		return hash(self) == hash(other)



db = DataBase('database.db')
for l in lst_in:
	db.write(Record(*,ap(str.strip, l.split(';'))))
