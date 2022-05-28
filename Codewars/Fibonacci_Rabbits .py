from functools import lru_cache


@lru_cache
def fib_rabbits(x, b):
    # your code here
    return fib_rabbits(x - 1, b) + b * fib_rabbits(x - 2, b) if x > 1 else x


def Fibonacci_Loop_Py(months, offsprings):
    parrent, child = 1, 1
    for i in range(months - 1):
        child, parrent = parrent, parrent + (child * offsprings)
    return child

