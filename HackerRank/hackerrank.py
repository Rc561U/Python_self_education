def solving(x):
    result = []
    for i in range(1,11):
        result.append(f'{x} * {i} = {x*i}')
    return result

if __name__ == '__main__':
    n = int(input().strip())
    res = (solving(n))
    for i in res: print(i)

