from collections import defaultdict
from queue import Queue


def find_max_distance():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)
        mapping[v].append(u)

    s = int(input())

    q = Queue()
    q.put(s)
    colors = ["white" for _ in range(n)]
    distances: list[int | None] = [None for _ in range(n)]
    distances[s - 1] = 0

    while q.qsize() > 0:
        v = q.get()

        for neighbor in mapping[v]:
            if colors[neighbor - 1] == "white":
                colors[neighbor - 1] = "grey"
                distances[neighbor - 1] = distances[v - 1] + 1
                q.put(neighbor)

        colors[v - 1] = "black"
        q.task_done()

    print(max(filter(lambda x: x is not None, distances)))


if __name__ == "__main__":
    find_max_distance()
