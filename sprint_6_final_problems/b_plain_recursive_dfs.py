from pprint import pprint


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)
ISLAND_ITEM = "#"
WATER_ITEM = "."


def dfs(i, j, matrix, n, m, visited_cells, size=0):
    if (
        i < 0
        or i >= n
        or j < 0
        or j >= m
        or matrix[i][j] == WATER_ITEM
        or (i, j) in visited_cells
    ):
        return 0

    visited_cells.add((i, j))

    for direction in DIRECTIONS:
        i_incr, j_incr = direction
        size += dfs(i + i_incr, j + j_incr, matrix, n, m, visited_cells)

    return size + 1


def calculate_the_number_and_the_max(matrix, n, m):
    visited_cells = set()
    number_of_islands = 0
    max_island_size = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == ISLAND_ITEM and (i, j) not in visited_cells:
                max_island_size = max(
                    dfs(i, j, matrix, n, m, visited_cells),
                    max_island_size,
                )
                number_of_islands += 1

    return number_of_islands, max_island_size


def solve():
    n, m = map(int, input().split())
    matrix = []

    for _ in range(n):
        matrix.append(input())

    return calculate_the_number_and_the_max(matrix, n, m)


if __name__ == "__main__":
    print(*solve())
