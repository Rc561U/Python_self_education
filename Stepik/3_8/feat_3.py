class Track:
	def __init__(self,x,y):
		self.start_x = x
		self.stary_y = y
		self.speed = None
		self.lst = []

	def __check_index(self,indx):
		if not (0 <= indx <= len(self.lst)-1) and not isinstance(indx,int):
			raise IndexError('некорректный индекс')

	def add_point(self,x,y,speed):
		self.lst.append([[x,y],[speed]])

	def __getitem__(self,indx):
		self.__check_index(indx)
		return self.lst[indx]
		
	def __setitem__(self,key,value):
		self.__check_index(key)
		self.lst[key][-1] = value

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError