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

    for value in mapping.values():
        value.sort()

    output_list = []
    explored = [False] * n
    explored[s - 1] = True
    d = deque()
    d.append(s)

    while len(d) > 0:
        c = d.popleft()
        output_list.append(c)

        for neighbor in mapping.get(c, []):
            if not explored[neighbor - 1]:
                explored[neighbor - 1] = True
                d.append(neighbor)

    return output_list


if __name__ == "__main__":
    print(*solve())
