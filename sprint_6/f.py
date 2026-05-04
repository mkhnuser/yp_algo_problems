from collections import deque


def solve():
    n, m = map(int, input().split())
    mapping = {}

    for _ in range(m):
        v, u = map(int, input().split())

        if v not in mapping:
            mapping[v] = []
        mapping[v].append(u)

        if u not in mapping:
            mapping[u] = []
        mapping[u].append(v)

    s, t = map(int, input().split())

    if s == t:
        return 0

    for value in mapping.values():
        value.sort()

    explored = [False] * n
    explored[s - 1] = True

    d = deque()
    d.append(s)
    distances = [0] * n
    distances[s - 1] = 0

    while len(d) > 0:
        c = d.popleft()

        for neighbor in mapping.get(c, []):
            if not explored[neighbor - 1]:
                distances[neighbor - 1] = distances[c - 1] + 1
                explored[neighbor - 1] = True
                d.append(neighbor)

    dist = distances[t - 1]
    return dist if dist != 0 else -1


if __name__ == "__main__":
    print(solve())
