import os


# Define again() Recursive function for Calculating Factorial
def factorial(n):
    return n * factorial(n - 1) if n > 1 else n


if __name__ == '__main__':
    print(int(input().strip()))
