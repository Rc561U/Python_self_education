class FileMaster():
    def __init__(self, filepath):
        #Your code here
        self.filepath = filepath.split('/')
    def extension(self):
        return self.filepath[-1].split('.')[-1]
        #Your code here
    def filename(self):
        #Your code here
        return self.filepath[-1].split('.')[0]
    def dirpath(self):
        #Your code here
        return '/'.join(self.filepath[:-1]+[''])


x = FileMaster('/Users/person1/Pictures/house.png')

print(x.extension(),x.filename(),x.dirpath())