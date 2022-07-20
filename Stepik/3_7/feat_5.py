class MailBox:
	def __init__(self):
		self.inbox_list = []

	def receive(self,st):
		self.inbox_list.append(st)

class MailItem:
	def __init__(self,mail,title,content):
		self.mail_from = mail
		self.title = title
		self.content = content
		self.is_read = False

	def set_read(self,fl_read=True):
		self.is_read = fl_read

	def __bool__(self):
		return self.is_read 

st_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!', 'mail@list.ru; Выгодное предложение; Вам одобрен кредит.', 'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
mail = MailBox()
for i,e in enumerate(st_in):
	mail_it,title,content = e.split(';')
	item = MailItem(mail_it,title,content)
	mail.receive(item)

mail.inbox_list[0].set_read()
mail.inbox_list[-1].set_read()

inbox_list_filtered = list(filter(lambda x:x, mail.inbox_list))
print(inbox_list_filtered)