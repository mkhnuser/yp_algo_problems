# NOTE: https://contest.yandex.ru/contest/22449/problems/C/.


def solve():
    n = int(input())  # NOTE: n rows.
    m = int(input())  # NOTE: m columns.

    matrix = []

    for _ in range(n):
        row = list(map(int, input().strip().split(" ")))
        matrix.append(row)

    x = int(input())  # NOTE: row coord.
    y = int(input())  # NOTE: column coords.

    elements_to_be_returned = []

    top_coords = (x - 1, y)
    buttom_coords = (x + 1, y)
    right_coords = (x, y + 1)
    left_coords = (x, y - 1)

    for x_coord, y_coord in (top_coords, buttom_coords, right_coords, left_coords):
        if 0 <= x_coord <= (n - 1) and 0 <= y_coord <= (m - 1):
            elements_to_be_returned.append(matrix[x_coord][y_coord])

    elements_to_be_returned.sort()
    return " ".join(str(el) for el in elements_to_be_returned)


if __name__ == "__main__":
    print(solve())
