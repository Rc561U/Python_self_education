class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values): return  False
        else:
            for name, value in zip(fields, lst_values):
                setattr(self, name, value)
            return True
class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = [44, 'Baby', 23 ]  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(data.__dict__, result)