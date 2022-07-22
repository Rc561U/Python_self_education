class SoftList(list):
	
	def __getitem__(self,item):
		try:
			return super().__getitem__(item)
		except IndexError:
			return False


sl = SoftList("python")
sl[0] # 'p'
sl[-1] # 'n'
sl[6] # False
print(sl[-7]) # False