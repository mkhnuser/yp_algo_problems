from collections import defaultdict


def solve_recursively():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        mapping[u].append(v)

    colors = ["white" for _ in range(n)]
    output = []

    for i in range(1, n + 1):
        if i not in mapping:
            # NOTE: i has no children, so to speak.
            mapping[i]

    def dfs(s):
        colors[s - 1] = "gray"

        for neighbor in mapping[s]:
            if colors[neighbor - 1] == "white":
                dfs(neighbor)

        colors[s - 1] = "black"
        output.append(s)

    def iterate():
        for i in range(1, n + 1):
            if colors[i - 1] == "white":
                dfs(i)

    iterate()
    output.reverse()
    print(*output)


if __name__ == "__main__":
    solve_recursively()
