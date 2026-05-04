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

    s = int(input())
    distances = [-1] * n
    distances[s - 1] = 0
    explored = [False] * n
    explored[s - 1] = True
    d = deque()
    d.append(s)

    while len(d) > 0:
        c = d.popleft()

        for v in mapping.get(c, []):
            if not explored[v - 1]:
                explored[v - 1] = True
                distances[v - 1] = distances[c - 1] + 1
                d.append(v)

    return max(distances)


if __name__ == "__main__":
    print(solve())
