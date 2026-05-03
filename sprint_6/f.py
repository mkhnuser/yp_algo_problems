from collections import defaultdict
from queue import Queue


def find_min_distance():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)
        mapping[v].append(u)

    s, t = map(int, input().split())

    q = Queue()
    q.put(s)
    colors = ["white" for _ in range(n)]
    distances: list[int | None] = [None for _ in range(n)]
    distances[s - 1] = 0
    # NOTE: To build path, you might want to use parents array.

    while q.qsize() > 0:
        v = q.get()

        for neighbor in mapping[v]:
            if colors[neighbor - 1] == "white":
                colors[neighbor - 1] = "grey"
                distances[neighbor - 1] = distances[v - 1] + 1
                q.put(neighbor)

        colors[v - 1] = "black"
        q.task_done()

    if distances[t - 1] is None:
        print(-1)
    else:
        print(distances[t - 1])


if __name__ == "__main__":
    find_min_distance()
