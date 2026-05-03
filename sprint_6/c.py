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
        mapping[v].append(u)

    s = int(input())

    for value in mapping.values():
        value.sort()

    colors = ["white" for _ in range(n)]
    output_list = []

    def dfs(s, output_list, mapping, colors):
        colors[s - 1] = "gray"
        output_list.append(s)

        for neighbor in mapping[s]:
            if colors[neighbor - 1] == "white":
                dfs(neighbor, output_list, mapping, colors)

        colors[s - 1] = "black"

    dfs(s, output_list, mapping, colors)
    print(*output_list)


def solve_visited_set_recursively():
    # NOTE: Hack your way through the limit.
    sys.setrecursionlimit(200000)

    n, m = map(int, input().split())
    adjacency_list = {}

    for _ in range(m):
        v, u = map(int, input().split())

        if v not in adjacency_list:
            adjacency_list[v] = []
        adjacency_list[v].append(u)

        if u not in adjacency_list:
            adjacency_list[u] = []
        adjacency_list[u].append(v)

    s = int(input())
    output_list = []

    visited = set()
    visited.add(s)

    for value in adjacency_list.values():
        value.sort()

    def dfs(v):
        output_list.append(v)

        for neighbor in adjacency_list.get(v, []):
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    dfs(s)
    return output_list


def solve_visited_set_iteratively():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)
        mapping[v].append(u)

    s = int(input())

    for value in mapping.values():
        value.sort()

    visited = set()
    output_list = []

    stack = [s]

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        output_list.append(current)
        visited.add(current)

        for neighbor in reversed(mapping[current]):
            if neighbor not in visited:
                stack.append(neighbor)

    print(*output_list)


def solve_if_elif_coloring():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)
        mapping[v].append(u)

    s = int(input())

    for value in mapping.values():
        value.sort()

    colors = ["white" for _ in range(n)]
    output_list = []

    stack = [s]

    while stack:
        current = stack.pop()
        if colors[current - 1] == "white":
            colors[current - 1] = "gray"
            stack.append(current)
            output_list.append(current)

            for neighbor in reversed(mapping[current]):
                if colors[neighbor - 1] == "white":
                    stack.append(neighbor)

        elif colors[current - 1] == "gray":
            colors[current - 1] = "black"

    print(*output_list)


if __name__ == "__main__":
    solve_if_elif_coloring()
