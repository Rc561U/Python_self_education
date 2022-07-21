class TriangleListIterator:
	def __init__(self,lst):
		self._lst = lst
				

	def __iter__(self):
		for i in range(len(self._lst)):
			for j in range(i+1):
				yield self._lst[i][j]


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x23', 'x24'],
       ['x30', 'x31', 'x32', 'x33']]



# for x in lst:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
#     print(x)

it_iter = iter(lst)
x = next(it_iter)
print(x)