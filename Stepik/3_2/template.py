class Counter:

	def __init__(self,chars):
		self.__counter = 0
		self.__chars = chars

	def __call__(self, *args, **kwargs):
		if not isinstance(args[0], str):
			raise TypeError('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')

		return args[0].strip(self.__chars)

s1 = Counter('?: @')
res = s1(' @@@he@llo?@')
print(res)