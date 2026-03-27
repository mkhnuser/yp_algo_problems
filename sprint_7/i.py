from pprint import pprint


def solve():
    n, m = map(int, input().split())
    points = []

    for _ in range(n):
        points.append(input())

    dp = [[0 for __ in range(m)] for _ in range(n)]
    dp.append([0 for _ in range(m)])
    for row in dp:
        row.insert(0, 0)

    for j in range(1, m + 1):
        for i in range(n - 1, -1, -1):
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + int(points[i][j - 1])

    total_points = dp[0][m]

    end_coords = (0, m)
    start_coords = (n - 1, 1)
    current_coords = end_coords
    reverse_path = []

    # NOTE: Dimensions: (n + 1) * (m + 1)

    while current_coords != start_coords:
        current_i, current_j = current_coords
        bottom_tile_coords = (current_i + 1, current_j)
        left_tile_coords = (current_i, current_j - 1)

        if bottom_tile_coords[0] >= (n + 1):
            current_coords = left_tile_coords
            reverse_path.append("R")
            continue

        if left_tile_coords[1] <= 0:
            current_coords = bottom_tile_coords
            reverse_path.append("U")
            continue

        bottom_tile_value = dp[bottom_tile_coords[0]][bottom_tile_coords[1]]
        left_tile_value = dp[left_tile_coords[0]][left_tile_coords[1]]

        if bottom_tile_value > left_tile_value:
            current_coords = bottom_tile_coords
            reverse_path.append("U")
        else:
            current_coords = left_tile_coords
            reverse_path.append("R")

    reverse_path.reverse()
    return total_points, reverse_path


if __name__ == "__main__":
    total_points, path = solve()
    print(total_points)
    print("".join(path))
