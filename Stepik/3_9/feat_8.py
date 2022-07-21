class StackObj:
	def __init__(self,data):
		self.data = data
		self.next = None

	def __repr__(self):
		return str(self.data)


class Stack:
	def __init__(self):
		self.top = None
		self.__last = None

	def push_back(self,obj):
		if self.top is None:
			self.top = obj
		else:
			self.__last.next = obj

		self.__last = obj 

	def push_front(self,obj):
		if self.top is None:
			self.__last = self.top = obj
		else:
			obj.next = self.top
			self.top = obj

	def _get_obj(self,indx):
		if not isinstance(indx,int) or not (0<= indx < len(self)):
			raise IndexError('неверный индекс')

		for i,obj in enumerate(self):
			if i == indx:
				return obj

	def __iter__(self):
		h = self.top
		while h:
			yield h
			h = h.next

	def __len__(self):
		return sum(1 for _ in self)

	def __getitem__(self,item):
		return self._get_obj(item).data

	def __setitem__(self,key,value):
		self._get_obj(key).data = value


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))
assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"