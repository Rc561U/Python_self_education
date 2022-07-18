class Viber:
	msg_list = {}
	
	@classmethod
	def add_message(cls, msg):
		cls.msg_list[id(msg)] = msg

	@classmethod
	def remove_message(cls,msg):
		key = id(msg)
		if key in cls.msg_list:
			cls.msg_list.pop(key)

	@classmethod
	def set_like(cls,msg):
		msg.fl_like = not msg.fl_like

	@classmethod
	def show_last_message(count):
		for i in tuple(cls.msg_list.values())[-count:]:
			print(m)
	@classmethod
	def total_messages(cls):
		return len(cls.msg_list)


class Message:
	def __init__(self,msg,like=False):
		self.text = msg
		self.fl_like = like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)