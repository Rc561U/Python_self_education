class Model:

	def __init__(self):
		self.fields = []

	def query(self,**kwargs):
		for k,v in kwargs.items():

			self.fields.append(f'{k} = {v}')

	def __str__(self):
		if len(self.fields) == 0:
			return "Model"
		return f"Model: {', '.join(self.fields)}"



model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model.fields)
print(model)


