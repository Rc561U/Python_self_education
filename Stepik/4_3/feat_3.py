class Book:
	def __init__(self,title, author, pages, year):
		self.title = title
		self.author = author
		self.pages = pages
		self.year = year


class DigitBook(Book):
	def __init__(self,title,author,pages,year,size,frm):
		super().__init__(title,author,pages,year)

		self.size = size
		self.frm = frm


db = DigitBook('title', 'author', 1000, 2000, 1345, 'pdf')
