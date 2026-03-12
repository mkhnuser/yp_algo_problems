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

    colors = [-1 for _ in range(n)]
    counter = 1

    def dfs(s, counter):
        colors[s - 1] = counter

        for neighbor in mapping[s]:
            if colors[neighbor - 1] == -1:
                dfs(neighbor, counter)

    def iterate(counter):
        for v in range(1, n + 1):
            if colors[v - 1] == -1:
                dfs(v, counter)
                counter += 1

    iterate(counter)
    present_the_result(colors)


def solve_visited_set():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)
        mapping[v].append(u)

    for i in range(1, n + 1):
        if i not in mapping:
            mapping[i]

    colors = [-1 for _ in range(n)]
    counter = 1

    def iterative_dfs(s, counter):
        stack = [s]
        while stack:
            current = stack.pop()

            if colors[current - 1] == -1:
                # NOTE: Has not been visited yet.
                colors[current - 1] = counter
                for neighbor in mapping[current]:
                    if colors[neighbor - 1] == -1:
                        # NOTE: Has not been visited yet.
                        stack.append(neighbor)

    def iterate(counter):
        for v in range(1, n + 1):
            if colors[v - 1] == -1:
                iterative_dfs(v, counter)
                counter += 1

    iterate(counter)
    present_the_result(colors)


def present_the_result(components):
    print(len(set(components)))
    components_index_to_nodes = defaultdict(list)

    for i, component_index in enumerate(components):
        v = i + 1
        components_index_to_nodes[component_index].append(v)

    nodes_clusters = list(components_index_to_nodes.values())

    for nodes in nodes_clusters:
        nodes.sort()

    nodes_clusters.sort(key=lambda x: x[0])

    for nodes in nodes_clusters:
        print(*nodes)


if __name__ == "__main__":
    solve_visited_set()
