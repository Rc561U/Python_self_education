class RenderList:

	def __init__(self, type_list):
		self.type_list = type_list if type_list in ("ul", "ol") else "ul"

	def __call__(self,st_list,*args, **kwargs):
		return '\n'.join([f"<{self.type_list}>",*map(lambda x:f"<li>{x}</li>",st_list), f"</{self.type_list}>"])


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)

print(html)