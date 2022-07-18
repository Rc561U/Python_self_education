
# counter = 0
# cells = [[ counter for j in range(5)] for i in range(3)]  			#list([Cell(0.0),Cell(0.0)]) 

# for i in cells:
# 	print(i)

import itertools
counter = itertools.count(1.0)
x = [[next(counter) for x in range(5)] for i in range(3)]

# for i in x:
# 	print(i)
class Cell:

	def __init__(self,value):
		self.value = value

class A:
	def __init__(self, N, M):
		
		counter = itertools.count(1.0)
		self.cells = [[Cell(next(counter)) for x in range(N)] for i in range(M)]

# 	def ret(self):
# 		return self.cells
# x = A(5,3)
# x = x.ret()
# for i in x:
# 	for j in i:
# 		print(j.value)