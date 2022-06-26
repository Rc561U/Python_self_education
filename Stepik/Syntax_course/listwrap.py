d = [1, 2, [True, False], ["Gomel", "Minsk", [100, 101], ['True', [-2, -1]]], 7.89]

# здесь продолжайте программу

def get_line_list(d, a=[]):
    [get_line_list(x, a) if isinstance(x,list) else a.append(x) for x in d]
    return a

print(list(get_line_list(d)))


def fib(x:int):
    return fib(x-1) + fib(x-2)  if x > 2 else x


print(fib(7))