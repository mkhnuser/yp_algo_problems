from collections import defaultdict
from queue import Queue


def bfs_impl():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)
        mapping[v].append(u)

    s = int(input())

    for value in mapping.values():
        value.sort()

    q = Queue()
    q.put(s)
    colors = ["white" for _ in range(n)]
    output = []

    while q.qsize() > 0:
        v = q.get()
        output.append(v)

        for neighbor in mapping[v]:
            if colors[neighbor - 1] == "white":
                colors[neighbor - 1] = "grey"
                # NOTE: Draw a square and understand why this setting is important.
                q.put(neighbor)

        colors[v - 1] = "black"
        q.task_done()

    print(*output)


if __name__ == "__main__":
    bfs_impl()
