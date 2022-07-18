class Clock:

	def __init__(self,time=0):
		self.__time = 0
		if self.__check_time(time):
			self.__time = time

	def set_time(self,tm):
		if __check_time(tm):
			self.__time = tm

	def get_time(self):
		return self.__time

	@classmethod
	def __check_time(cls,tm):
		return type(tm)==int and 100000 > tm >= 0

clock = Clock(4530)
print(clock.get_time())