import sys
from collections import defaultdict


def solve_recursively():
    # NOTE: Hack your way through.
    sys.setrecursionlimit(200000)
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)

    s = 1
    time = -1
    entry: list[int | None] = [None for _ in range(n)]
    leave: list[int | None] = [None for _ in range(n)]
    colors = ["white" for _ in range(n)]

    for value in mapping.values():
        value.sort()

    def dfs(s):
        nonlocal time
        time += 1
        colors[s - 1] = "gray"
        entry[s - 1] = time

        for neighbor in mapping[s]:
            if colors[neighbor - 1] == "white":
                dfs(neighbor)

        time += 1
        colors[s - 1] = "black"
        leave[s - 1] = time

    dfs(s)

    for e, l in zip(entry, leave):
        print(e, l)


def solve_if_elif_coloring():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)

    s = 1
    time = -1
    entry: list[int | None] = [None for _ in range(n)]
    leave: list[int | None] = [None for _ in range(n)]
    colors = ["white" for _ in range(n)]

    for value in mapping.values():
        value.sort()

    stack = [s]
    while stack:
        v = stack.pop()

        if colors[v - 1] == "white":
            colors[v - 1] = "gray"
            time += 1
            entry[v - 1] = time
            stack.append(v)

            for neighbor in reversed(mapping[v]):
                if colors[neighbor - 1] == "white":
                    stack.append(neighbor)

        elif colors[v - 1] == "gray":
            colors[v - 1] = "black"
            time += 1
            leave[v - 1] = time

    for e, l in zip(entry, leave):
        print(e, l)


def solve_visited_set():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)

    s = 1
    time = -1
    entry: list[int | None] = [None for _ in range(n)]
    leave: list[int | None] = [None for _ in range(n)]
    visited = set()

    for value in mapping.values():
        value.sort()

    stack = [s]
    while stack:
        v = stack.pop()

        if v in visited:
            if leave[v - 1] is None:
                time += 1
                leave[v - 1] = time
            continue

        visited.add(v)
        time += 1
        entry[v - 1] = time
        stack.append(v)

        for neighbor in reversed(mapping[v]):
            if neighbor not in visited:
                stack.append(neighbor)

    for e, l in zip(entry, leave):
        print(e, l)


if __name__ == "__main__":
    solve_visited_set()
