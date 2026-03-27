def solve_iteratively():
    n = int(input())
    modulus = (10**9) + 7

    if n == 0 or n == 1:
        return 1

    # NOTE: n >= 2.
    a, b = 1, 1
    n -= 2

    while n >= 0:
        a, b = b, (a + b) % modulus
        n -= 1

    return b


if __name__ == "__main__":
    print(solve_iteratively())
