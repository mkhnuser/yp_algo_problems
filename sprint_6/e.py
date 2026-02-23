from collections import defaultdict


def solve_recursively():
    # NOTE: This fails the recursion limit.
    mapping = defaultdict(list)
    n, m = map(int, input().split())

    for _ in range(m):
        v, u = map(int, input().split())
        mapping[v].append(u)
        mapping[u].append(v)

    for i in range(1, n + 1):
        if i not in mapping:
            mapping[i]

    components_counter = 1
    colors = [-1 for _ in range(n)]

    def dfs(v):
        colors[v - 1] = components_counter

        for adj_vertex in mapping[v]:
            if colors[adj_vertex - 1] == -1:
                dfs(adj_vertex)

    for v, color in enumerate(colors, start=1):
        if color == -1:
            dfs(v)
            components_counter += 1

    print(len(set(colors)))

    color_groups = defaultdict(list)

    for vertex, color in enumerate(colors, start=1):
        color_groups[color].append(vertex)

    for vertex_group in color_groups.values():
        vertex_group.sort()

    for vertex_group in sorted(color_groups.values(), key=lambda g: g[0]):
        print(*vertex_group)


def solve_iteratively():
    mapping = defaultdict(list)
    n, m = map(int, input().split())

    for _ in range(m):
        v, u = map(int, input().split())
        mapping[v].append(u)
        mapping[u].append(v)

    for i in range(1, n + 1):
        if i not in mapping:
            mapping[i]

    components_counter = 1
    colors = [-1 for _ in range(n)]

    def dfs(v):
        stack = [v]
        colors[v - 1] = components_counter

        while stack:
            c = stack.pop()

            for adj_vertex in mapping[c]:
                if colors[adj_vertex - 1] == -1:
                    colors[adj_vertex - 1] = components_counter
                    stack.append(adj_vertex)

    for v, color in enumerate(colors, start=1):
        if color == -1:
            dfs(v)
            components_counter += 1

    print(len(set(colors)))

    color_groups = defaultdict(list)

    for vertex, color in enumerate(colors, start=1):
        color_groups[color].append(vertex)

    for vertex_group in color_groups.values():
        vertex_group.sort()

    for vertex_group in sorted(color_groups.values(), key=lambda g: g[0]):
        print(*vertex_group)


if __name__ == "__main__":
    solve_iteratively()
