import random
class Line:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d

choice = random.randint(0, 2)
a, b, c, d = [random.randrange(1, 1000) for i in range(4)]

elements = []
for i in range(217):
    elements.append([Line(a, b, c, d), Rect(a, b, c, d), Ellipse(a, b, c, d)][choice])

elements = [Line(0, 0, 0, 0) if isinstance(i, Line) else i for i in elements]
