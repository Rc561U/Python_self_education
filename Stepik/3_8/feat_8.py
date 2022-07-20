class TicTacToe:
	def __init__(self):
		self._n = 3
		self.pole = tuple(tuple(Cell() for _ in range(self._n)) for _ in range(self._n))

	def clear(self):
		for i in self.pole:
			for cell in i:
				cell.is_free = True
				cell.value = 0

	def __check(self,item):
		if not isinstance(item, tuple) or len(item)!=2:
			raise IndexError('неверный индекс клетки')
		if any(not (0 <= x < self._n)for x in item if type(x) != slice):
			raise IndexError('неверный индекс клетки')

	def __setitem__(self,key,value):
		self.__check(key)
		r,c = key
		if self.pole[r][c]:
			self.pole[r][c].value = value
			self.pole[r][c].is_free = False
		else:
			raise ValueError('клетка уже занята')

	def __getitem__(self,item):
		self.__check(item)
		r,c = item
		if type(r) == slice:
			return tuple(self.pole[x][c].value for x in range(self._n))
		if type(c) == slice:
			return tuple(self.pole[r][x].value for x in range(self._n))

		return self.pole[r][c].value 


class Cell:
	def __init__(self):
		self.is_free = True
		self.value = 0

	def __bool__(self):
		return self.is_free





g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    
try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"


g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"