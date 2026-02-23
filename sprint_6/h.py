from collections import defaultdict
from typing import TypeAlias


def solve_recursively():
    # NOTE: Starting from s, you have access to all the nodes of a graph.
    # Begin at s, find entry time and leave time.
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        v, u = map(int, input().split())
        mapping[v].append(u)

    for value in mapping.values():
        value.sort()

    s = 1
    time = -1
    colors = ["white" for _ in range(n)]
    entry = [None for _ in range(n)]
    leave = [None for _ in range(n)]

    def dfs(v, time, colors, entry, leave):
        colors[v - 1] = "gray"
        time += 1
        entry[v - 1] = time

        for neighbor in mapping[v]:
            if colors[neighbor - 1] == "white":
                _, time, colors, entry, leave = dfs(
                    neighbor, time, colors, entry, leave
                )

        time += 1
        leave[v - 1] = time
        colors[v - 1] = "black"

        return v, time, colors, entry, leave

    dfs(s, time, colors, entry, leave)

    for i in range(n):
        print(f"{entry[i]} {leave[i]}")


def solve_iteratively():
    # NOTE: Starting from s, you have access to all the nodes of a graph.
    # Begin at s, find entry time and leave time.
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        v, u = map(int, input().split())
        mapping[v].append(u)

    for value in mapping.values():
        value.sort()

    s = 1
    time = -1
    colors = ["white" for _ in range(n)]
    entry: list[None | int] = [None for _ in range(n)]
    leave: list[None | int] = [None for _ in range(n)]
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
        else:
            # NOTE: Do nothing with a black one.
            pass

    for i in range(n):
        print(f"{entry[i]} {leave[i]}")


if __name__ == "__main__":
    solve_iteratively()
