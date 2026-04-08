def prefix_function(s):
    n = len(s)
    pr: list[int | None] = [None] * n
    pr[0] = 0

    for i in range(1, n):
        k = pr[i - 1]
        while k > 0 and s[k] != s[i]:
            k = pr[k - 1]
        if s[k] == s[i]:
            k += 1
        pr[i] = k

    return pr


if __name__ == "__main__":
    print(*prefix_function(input()))
