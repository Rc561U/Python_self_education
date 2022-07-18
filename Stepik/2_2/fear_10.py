class PhoneBook:
	def __init__(self):
		self.phonebook = list()

	def add_phone(self,phone):
		self.phonebook.append(phone)
	def remove_phone(self,indx):
		del self.phonebook[indx]
	def get_phone_list(self):
		return self.phonebook


class PhoneNumber:
	def __init__(self,number,name):
		self.number = number
		self.name = name


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones[1].name)