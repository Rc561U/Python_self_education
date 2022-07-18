class WindowDlg:

	def __init__(self,title,width,height):
		self.__title = title
		self.__width = self.__height = None
		self.width = width
		self.height = height

	
	def show(self):
		print(f'{self.__title}: {self.__width}, {self.__height}')

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self,newidth):
		if type(newidth)==int and 0 <= newidth <= 10000:
			if self.__width:
				self.show()
			self.__width = newidth

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self,newheight):
		if type(newheight)==int and 0 <= newheight <= 10000:
			if self.__height:
				self.show()
			self.__height = newheight

	

w = WindowDlg("title", 23, 23)

w.width = "123"

print(w.__dict__)