class TriangleChecker :
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self) -> int:
        checker = sorted([self.a, self.b, self.c])
        a, b, c = checker
        for i in checker:
            if i < 0 or i == 0: return 1
        if a + b <= c: return 2
        return 3


# a, b, c = map(int, input().split())
tr = TriangleChecker(3, 4, 5)
print(tr.is_triangle())
