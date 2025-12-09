# NOTE: Memoization does not help us to compute n = 10 ** 6.
# memo = {}
#
#
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#
#     if n in memo:
#         return memo[n]
#
#     memo[n] = fib(n - 1) + fib(n - 2)
#     return memo[n]


def fib(n):
    a, b = 1, 1

    # 1 1 2 3 5 8 13
    # 0 1 2 3 4 5 6

    if n == 0 or n == 1:
        return 1

    assert n >= 2

    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c

    return c


def solve():
    n, k = map(int, input().split())
    return fib(n) % (10**k)


if __name__ == "__main__":
    print(solve())
