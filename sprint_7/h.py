def solve_truly():
    n, m = map(int, input().split())

    # NOTE:
    # 2 3
    # 101
    # 110
    # DP matrix:
    # [
    # [0, 0, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 0, 0]
    # ]
    # Populated DP matrix:
    # [
    # [0, 2, 2, 3],
    # [0, 1, 2, 2],
    # [0, 0, 0, 0]
    # ]
    # 3

    points = []
    for _ in range(n):
        points.append(input())

    dp = [[0 for __ in range(m)] for _ in range(n)]

    # NOTE: Add gutters to the left and at the buttom.
    dp.append([0 for __ in range(m)])
    for row in dp:
        row.insert(0, 0)

    # NOTE: Constraints: you can only move up or to the right.
    # You start at the buttom left and move to the top right.

    # WARNING: Since gutters have been added, boundaries have been shift as well.

    for j in range(1, m + 1):
        for i in range(n - 1, -1, -1):
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + int(points[i][j - 1])

    return dp[0][m]


def solve_falsely():
    # BUG: This solution is wrong since it produces an invalid dp array by starting off an invalid index.
    n, m = map(int, input().split())

    # NOTE:
    # 2 3
    # 101
    # 110
    # [
    # [-inf, 0, 0, 0],
    # [-inf, 0, 0, 0],
    # [-inf, -inf, -inf, -inf],
    # ]
    #
    # [
    # [2, 2, 3, 0],
    # [1, 2, 2, 0],
    # [-inf, -inf, -inf, -inf]
    # ]
    #
    # 3

    points = []
    for _ in range(n):
        points.append(input())

    dp = [[0 for __ in range(m)] for _ in range(n)]
    dp.append([float("-inf") for __ in range(m)])
    for row in dp:
        row.insert(0, float("-inf"))

    # NOTE: Constraints: you can only move up or to the right.
    # You start at the buttom left and move to the top right.

    for j in range(0, m):
        for i in range(n - 1, -1, -1):
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + int(points[i][j])

    return dp[0][m - 1]


if __name__ == "__main__":
    print(solve_truly())
