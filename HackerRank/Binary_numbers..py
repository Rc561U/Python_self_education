import re

def finder(x):
    # return consecutive of '1' in stdin number
    count = []
    x = str(bin(x))
    if '11' not in x: return 1
    else: count.append(re.findall('[1]*', x ))
    result = sorted(*count)
    return len(result[-1])

if __name__ == '__main__':
    n = int(input().strip())
    print(finder(n))