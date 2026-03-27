import sys


def solve_recursively():
    # NOTE: Try to hack your way through recursion.
    sys.setrecursionlimit(200000)
    n, k = map(int, input().split())
    # NOTE: Use zero-based counting.
    n -= 1
    modulus = (10**9) + 7
    mapping = {}

    return recurse(n, k, mapping) % modulus


def recurse(n, k, mapping):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1

    if n in mapping:
        return mapping[n]

    number_of_ways = 0
    for t in range(1, k + 1):
        number_of_ways += recurse(n - t, k, mapping)

    mapping[n] = number_of_ways
    return number_of_ways


def solve_iteratively():
    n, k = map(int, input().split())
    # NOTE: Use zero-based counting: treat the first step as 0, the second as 1, etc.
    n -= 1
    modulus = (10**9) + 7

    dp: list[int | None] = [None for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1

    # NOTE: For each yet unvisited step of our staircase,
    # Look k steps back,
    # Accumulate the number of ways to get there,
    # Assign this number to the current step.
    for i in range(2, n + 1):
        acc = 0
        for j in range(i - 1, i - k - 1, -1):
            if j < 0:
                # NOTE: But don't look too far!
                break

            acc += dp[j]
        dp[i] = acc

    return dp[n] % modulus


if __name__ == "__main__":
    print(solve_iteratively())
