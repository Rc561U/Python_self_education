class Translator:

    def add(self, eng, rus):
        if hasattr(self, eng):
            self.__dict__[eng].append(rus)
        else:  setattr(self, eng, [rus])
    # def add(self, eng, rus):
    #     self.dict_eng.setdefault(eng, []).append(rus)

    def remove(self, eng): delattr(self,eng)

    def translate(self, eng): return getattr(self, eng)



s = '''
tree - дерево
car - машина
car - автомобиль
leaf - лист
river - река
go - идти
go - ехать
go - ходить
milk - молоко
'''
if __name__ == '__main__':
    tr = Translator()
    for i in s.split('\n'):
        if i:
            k, v = i.split(' - ')
            tr.add(k, v)
    tr.remove('car')
    print(*tr.translate('go'))
