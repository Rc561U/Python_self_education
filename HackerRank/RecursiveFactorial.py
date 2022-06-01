import os


# Define again() Recursive function for Calculating Factorial
# def factorial(n):
#     return n * factorial(n - 1) if n > 1 else n
#
#
# if __name__ == '__main__':
#     print(int(input().strip()))



def fac(n):
    return n * fac(n-1) if n > 1 else n

def zeros(n):
    fact = str(fac(n))
    if fact.count('0'): return 0
    while '00' in fact:
        fact = fact.replace('00', '0')
    return fact.count('0')

print(zeros(6))