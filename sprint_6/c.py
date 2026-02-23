def solve():
    n, m = map(int, input().split())

    # NOTE: Use only a half of a matrix because of a memory limit.
    adjacency_matrix = []
    for i in range(1, n + 1):
        adjacency_matrix.append([False for _ in range(i)])

    for _ in range(m):
        u, v = map(int, input().split())
        try:
            adjacency_matrix[u - 1][v - 1] = True
        except Exception:
            pass

        try:
            adjacency_matrix[v - 1][u - 1] = True
        except Exception:
            pass

    s = int(input())

    # NOTE:
    # 4 4
    # 3 2
    # 4 3
    # 1 4
    # 1 2
    # 3
    # [
    #     [False],
    #     [True, False],
    #     [False, True, False],
    #     [True, False, True, False],
    # ]

    colors = ["white" for _ in range(n)]

    def start_dfs():
        for index in range(n):
            if colors[index] == "white":
                dfs(index + 1)

    def dfs(v):
        # NOTE: v is the node value, but not its index!
        colors[v - 1] = "gray"

        print(v, end=" ")

        for i, w in enumerate(adjacency_matrix[v - 1], start=1):
            if not w:
                continue

            if colors[i - 1] == "white":
                dfs(i)

        # NOTE: Also go over v - 1 column.
        for i, row in enumerate(range(v - 1, n), start=1):
            w = adjacency_matrix[row][v - 1]

            if not w:
                continue

            if colors[i - 1] == "white":
                dfs(i)

        colors[v - 1] = "black"

    dfs(s)


if __name__ == "__main__":
    solve()
