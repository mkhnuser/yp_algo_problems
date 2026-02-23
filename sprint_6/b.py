def solve():
    n, m = map(int, input().split())
    adjacency_matrix = [[0 for __ in range(n)] for _ in range(n)]

    for _ in range(m):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        adjacency_matrix[i][j] = 1

    for row in adjacency_matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    solve()
