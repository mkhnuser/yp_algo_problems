def main():
    n = int(input())
    g = list(map(int, input().split()))
    m = int(input())
    c = list(map(int, input().split()))

    g.sort()
    c.sort()

    counter = 0

    # NOTE: g is the subsequence.
    # and c is the main sequence.

    sub = 0
    p = 0

    while p < len(c) and sub < len(g):
        if g[sub] <= c[p]:
            counter += 1
            sub += 1

        p += 1

    return counter


if __name__ == "__main__":
    print(main())
