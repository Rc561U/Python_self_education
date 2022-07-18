import re
from string import ascii_lowercase, ascii_uppercase, digits
import random

class EmailValidator:
	CREATE_EMAIL = ascii_uppercase + ascii_lowercase + '_-.'
	def __new__(cls,*args,**kwargs):
		return None

	@classmethod
	def check_email(cls,email):
		pattern = ("\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}")
		if not cls.__is_email_str(email):
			return False
        
		ss = email.split("@")
		if len(ss) != 2:
			return False

		if len(ss[0]) > 100 and len(ss[1]) > 50:
			return False

		if not re.search(pattern,email):
			return False
        
		if email.count('..') > 0:
			return False
        
		return True


	@classmethod
	def get_random_email(cls):
		num = random.choice(range(4,20))
		em = ''
		for i in range(num):
			em += random.choice(cls.CREATE_EMAIL)
		return em+'@gmail.com'


	@staticmethod
	def __is_email_str(email):
		return type(email)==str








res = EmailValidator.check_email("sc..lib@list.ru") 
print(res)# True
res = EmailValidator.get_random_email()
print(res)
print(EmailValidator.check_email(res))