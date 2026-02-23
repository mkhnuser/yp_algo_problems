from collections import defaultdict


def solve():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        start, end = map(int, input().split())
        mapping[start].append(end)

    # NOTE: Populate isolated nodes.
    for i in range(1, n + 1):
        if i not in mapping:
            mapping[i]

    # NOTE: Topological sorting of a DAG is a sorting by leave time reversed.
    colors = ["white" for _ in range(n)]
    output: list[int] = []

    def dfs(v):
        colors[v - 1] = "gray"

        for adjacent_vertex in mapping[v]:
            if colors[adjacent_vertex - 1] == "white":
                dfs(adjacent_vertex)

        colors[v - 1] = "black"
        output.append(v)

    def iterate():
        for v in mapping:
            if colors[v - 1] == "white":
                dfs(v)

    iterate()
    output.reverse()
    print(*output)


if __name__ == "__main__":
    solve()
