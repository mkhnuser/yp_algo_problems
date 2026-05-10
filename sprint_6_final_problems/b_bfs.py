from pprint import pprint
from collections import deque


DIRECTIONS = (
    (0, +1),  # top
    (+1, 0),  # right
    (0, -1),  # buttom
    (-1, 0),  # left
)
ISLAND_ITEM = "#"
WATER_ITEM = "."


def bfs(i, j, matrix, n, m, visited_cells):
    d = deque()
    d.append((i, j))
    visited_cells.add((i, j))

    size = 0

    while d:
        i, j = d.popleft()
        size += 1

        for i_incr, j_incr in DIRECTIONS:
            next_i = i + i_incr
            next_j = j + j_incr

            if (
                next_i < 0
                or next_i >= n
                or next_j < 0
                or next_j >= m
                or matrix[next_i][next_j] == WATER_ITEM
                or (next_i, next_j) in visited_cells
            ):
                continue

            d.append((next_i, next_j))
            visited_cells.add((next_i, next_j))

    return size


def calculate_the_number_and_the_max(matrix, n, m):
    visited_cells = set()
    number_of_islands = 0
    max_island_size = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == ISLAND_ITEM and (i, j) not in visited_cells:
                max_island_size = max(
                    bfs(i, j, matrix, n, m, visited_cells),
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
