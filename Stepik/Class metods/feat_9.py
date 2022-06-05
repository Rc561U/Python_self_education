
class DataBase:
    data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for string in data:
            self.data.append(dict(zip(self.FIELDS, string.split())))

    def select(self, a, b):
        # check = map(str, list(range(a,b+1)))
        # new = [i for i in self.data if i['id'] in check]
        return self.data[a:b+1]


lst = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
db = DataBase()
db.insert(lst)
x = db.select(1,3)
for i in x:
    print(i)
