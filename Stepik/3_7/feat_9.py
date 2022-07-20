class Vector:
	def __init__(self,*args):
		self.coords = list(args)

	def __get_true_sequences(self,other):
		if not len(self) == len(other):
			raise ArithmeticError('размерности векторов не совпадают')

	def __len__(self):
		return len(self.coords)


	def __add__(self,other):
		if len(self.coords) == len(other.coords):
			return Vector(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])
		else: raise ArithmeticError('размерности векторов не совпадают')
	def __sub__(self,other):
		if len(self.coords) == len(other.coords):
			return Vector(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])
		else: raise ArithmeticError('размерности векторов не совпадают')	
	def __mul__(self,other):
		if len(self.coords) == len(other.coords):
			return Vector(*[self.coords[i] * other.coords[i] for i in range(len(self.coords))])
		else: raise ArithmeticError('размерности векторов не совпадают')	
	
	def __iadd__(self,other):
		if isinstance(other,Vector):
			self.coords=[self.coords[i] + other.coords[i] for i in range(len(self.coords))]
			return self
		self.coords = [i+other for i in self.coords]
		return self

	def __isub__(self,other):
		if isinstance(other,Vector):
			self.coords=[self.coords[i] - other.coords[i] for i in range(len(self.coords))]
			return self
		self.coords = [i-other for i in self.coords]
		return self

	def __bool__(self,other):
		return any([ x1[i] == x2[i] for i in range(len(x1))])
		


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(hash(v1))
print(hash(v1+v2))
v1+=10
v1 += v2
print(hash(v1))
# print((v1 + v2).coords)  # [5, 7, 9]
# print((v1 - v2).coords)  # [-3, -3, -3]
# print((v1 * v2).coords)  # [4, 10, 18]


# v1 += 10
# print(v1.coords)  # [11, 12, 13]
# v1 -= 10
# print(v1.coords)  # [1, 2, 3]
# v1 += v2
# print(v1.coords)  # [5, 7, 9]
# v2 -= v1
# print(v2.coords)  # [-1, -2, -3]

# print(v1 == v2)  # False
# print(v1 != v2)  # True