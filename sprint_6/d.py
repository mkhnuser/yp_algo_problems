from collections import defaultdict
from queue import Queue


def solve():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)
        mapping[v].append(u)

    for value in mapping.values():
        value.sort()

    s = int(input())
    colors = ["white" for _ in range(n)]
    distances: list[None | int] = [None for _ in range(n)]
    parents: list[None | int] = [None for _ in range(n)]

    q = Queue()
    q.put(s)
    colors[s - 1] = "gray"
    distances[s - 1] = 0
    parents[s - 1] = None

    while not q.empty():
        c = q.get()
        print(c, end=" ")

        for adj in mapping[c]:
            if colors[adj - 1] != "white":
                continue

            q.put(adj)
            colors[adj - 1] = "gray"
            distances[adj - 1] = distances[c - 1] + 1
            parents[adj - 1] = c

        colors[c - 1] = "black"
        q.task_done()


if __name__ == "__main__":
    solve()
