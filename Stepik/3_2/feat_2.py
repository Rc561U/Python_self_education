import random

class RandomPassword:

	def __init__(self,psw_chars,min_lenght,max_lenght):
		self.psw_chars = psw_chars
		self.min_lenght = min_lenght
		self.max_lenght = max_lenght


	def __call__(self,*args, **kwargs):
		lenght = random.choice(range(self.min_lenght,self.max_lenght))
		result = [random.choice(self.psw_chars) for i in range(lenght)]
		return ''.join(result)



min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)

psw = rnd()
lst_pass = [rnd() for i in range(3)]
print(lst_pass)