class Body:
	def __init__(self,name,ro,volume):
		self.name = name
		self.mas = ro * volume

	def __eq__(self,other):
		m = other.mas if isinstance(other,Body) else other
		return self.mas == m

	def __lt__(self,other):
		m = other.mas if isinstance(other,Body) else other
		return self.mas < m
	def __gt__(self,other):

		m = other.mas if isinstance(other,Body) else other
		return self.mas > m


body1,body2 = Body("anton", 12, 230),Body("anton", 12, 230)
body1 > body2  # True, если масса тела body1 больше массы тела body2
print(body1 == body2) # True, если масса тела body1 равна массе тела body2
print(body1 < 10)     # True, если масса тела body1 меньше 10
print(body2 == 5)     # True, если масса тела body2 равна 5