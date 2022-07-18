class AppStore:

	def __init__(self):
		self.app_dict = {}


	def add_application(self, app):
		self.app_dict[id(app)] = app

	def remove_application(self, app):
		self.app_dict.pop(id(app))


	def block_application(self, app):
		obj = self.app_dict.get(id(app), False)
		if not obj:
			return False
		obj.blocked = True
		return True

	def total_apps(self):
		return len(self.app_dict)


class Application:
	def __init__(self,name):
		self.name = name
		self.blocked = False



store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)