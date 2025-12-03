# NOTE: Magic.
def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


def solve():
    num = int(input())
    primes = get_least_primes_linear(10**9)[0]
    res = []

    for prime in primes:
        q, r = divmod(num, prime)

        while r == 0:
            res.append(prime)
            q, r = divmod(q, prime)

    return " ".join(map(str, res))


if __name__ == "__main__":
    print(solve())
