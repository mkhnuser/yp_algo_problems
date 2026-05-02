def main():
    n = int(input())
    g = list(map(int, input().split()))
    m = int(input())
    c = list(map(int, input().split()))

    g.sort()
    c.sort()

    i = 0
    j = 0

    # NOTE: Suppose c is the main sequence.
    while j < len(c) and i < len(g):
        if g[i] <= c[j]:
            i += 1

        j += 1

    return i


if __name__ == "__main__":
    print(main())
