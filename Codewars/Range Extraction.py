from itertools import groupby
def remark(x):
    return f'{x[0]}-{x[-1]}'

def solution(x):
    new = []
    for _, g in groupby(enumerate(x), lambda x: x[0] - x[1]):
        new.append([x for i,x in g])
    meu =[]
    for i in new:
        if len(i) > 2:
            meu.append(remark(i))
        else:
            [meu.append(str(ss)) for ss in i]

    return ','.join(meu)

