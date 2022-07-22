class ItemAttrs:
	def __getitem__(self,item):
		lst = list(self.__dict__.values())
		return lst[item]

	def __setitem__(self,key,value):
		
		self.__dict__.update(key,value)

class Point(ItemAttrs):
	def __init__(self,x,y):
		self.x = x
		self.y = y


pt = Point(1, 2.5)

x = pt[0]
print(x)  # 1
y = pt[1] 
print(y)  # 2.5
pt[0] = 10
print(pt.__dict__)