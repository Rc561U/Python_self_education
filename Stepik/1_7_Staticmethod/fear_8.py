from string import ascii_lowercase, digits
import re

class CardCheck:
	
	@staticmethod
	def check_card_number(number):
		return bool(re.fullmatch(r"(?:\d{4}-?){3}\d{4}",number))
		

	@staticmethod
	def check_name(name):
		return bool(re.fullmatch(r"[A-Z\d]+ [A-Z\d]+", name))


	

is_number = CardCheck.check_card_number("1234-5678-9012-000a0")
is_name = CardCheck.check_name("SERGEI BALAKIREV G")
print(is_number)
print(is_name)