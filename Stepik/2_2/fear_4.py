class Car:

	def __init__(self):
		self.__model = None

	@property
	def model(self):
		return self.__model

	@model.setter
	def model(self,model:input):
		if self.check_model(model):
			self.__model = model


	@classmethod
	def check_model(cls,model):
		if not type(model)==str:
			return False
		elif not 2 < len(model) < 100:
			return False
		return True

	


car = Car()
car.model = "ta"

print(car.__dict__)