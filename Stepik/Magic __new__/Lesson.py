class Poin:
    def __new__(cls, *args, **kwargs):
        print('call __new__  for ' + str(cls))
        return super().__new__(cls)
    def __init__(self, x=0, y=0):
        print("call __init__ for" + str(self))
        self.x = x
        self.y = y


pt = Poin(1,2)
print(pt)

class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, usrt, psw, port):
        self.user = usrt
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'connect to DB: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print("close the DB")

    def read(self):
        return 'date from DB'

    def write(self, data):
        print(f' write into DB {data}')

db = DataBase('root', '123', 90)
db2 = DataBase('root2', '56312', 40)
print(id(db),id(db2))
