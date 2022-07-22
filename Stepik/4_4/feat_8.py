class Aircraft:
	def __init__(self,model, mass, speed, top):
		self.__check_value(model, mass, speed, top)
		self._model = model 
		self._mass = mass
		self._speed = speed 
		self._top = top



	@staticmethod
	def __check_value(model, mass, speed, top):
		if type(model) != str or not all(isinstance(x,(int,float))and x > 0  for x in [mass, speed, top]):
			raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
	def __init__(self,model, mass, speed, top, chairs):
		super().__init__(model,mass,speed,top)
		self.__check_value(chairs)
		self._chairs = chairs

	@staticmethod
	def __check_value(x):
		if not isinstance(x,int) or x <= 0:
			raise TypeError('неверный тип аргумента')

class WarPlane(Aircraft):
	def __init__(self,model, mass, speed, top, weapons):
		super().__init__(model,mass,speed,top)
		self.__check_value(weapons)
		self._weapons = weapons

	@staticmethod
	def __check_value(x):
		if not isinstance(x,dict):
			raise TypeError('неверный тип аргумента')
		for k,v in x.items():
			if type(v) != int and type(k) != str:
				raise TypeError('неверный тип аргумента')
		


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]


PassengerAircraft('model', 1, 2, 3, 1.2)