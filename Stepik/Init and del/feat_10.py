class Cell:
    def __init__(self, mines, mine):
        self.around_mines  = mines
        self.mine = mine
        self.fl_open = False
class GamePole:
    def __init__(self, n, m):
        self.n = n
        self.m = m


for i in range(5):
    for i in range(5):
        print('*', end=' ')
    print( )