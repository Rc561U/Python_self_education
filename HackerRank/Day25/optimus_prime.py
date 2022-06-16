def is_prime(n: int) -> bool:
    if n <= 1: return False
    for i in range(2, int(n ** .5 + 1)):
        if n % i == 0: return False
    return True


if __name__ == "__main__":
    for i in range(int(input())):
        x = (is_prime(int(input())))
        print("Not prime" if not x else "Prime")
