from collections import defaultdict


def solve():
    n = int(input())
    S = int(input())
    arr = list(map(int, input().split()))

    pair_sum = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            pair_sum[arr[i] + arr[j]].append((i, j))

    result = set()

    for s in pair_sum:
        t = S - s
        if t not in pair_sum:
            continue

        for i, j in pair_sum[s]:
            for k, l in pair_sum[t]:
                if len({i, j, k, l}) == 4:
                    quad = sorted([arr[i], arr[j], arr[k], arr[l]])
                    result.add(tuple(quad))

    return sorted(result)


if __name__ == "__main__":
    res = solve()
    print(len(res))

    for q in res:
        print(" ".join(map(str, q)))
