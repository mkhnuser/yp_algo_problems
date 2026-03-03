from pprint import pprint


def find_starting_point(matrix):
    for i, row in enumerate(matrix):
        if "*" not in row:
            continue

        for j, char in enumerate(row):
            if char == "*":
                return (i, j)

    return (None, None)


def compute_exit_paths(i, j, current_path, visited, exit_paths, matrix):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        # NOTE: The current recursive call is out of bound.
        return

    current_num = matrix[i][j]

    if current_num == "1":
        # NOTE: The current recursive call is invalid.
        return

    if (i, j) in visited:
        return

    current_path.append((i, j))
    visited.add((i, j))

    if current_num == "0" and (
        i == 0 or i == (len(matrix) - 1) or j == 0 or j == (len(matrix[0]) - 1)
    ):
        exit_paths.append(current_path.copy())
    else:
        top = (i - 1, j)
        right = (i, j + 1)
        bottom = (i + 1, j)
        left = (i, j - 1)

        for direction in (top, right, bottom, left):
            next_i, next_j = direction
            compute_exit_paths(
                next_i,
                next_j,
                current_path,
                visited,
                exit_paths,
                matrix,
            )

    # NOTE: When we backtrack,
    # We are guaranteed not to visit this node again within a concrete recursive step.
    current_path.pop()
    visited.remove((i, j))


def main():
    matrix = [
        "1100111",
        "1001*01",
        "1011011",
        "1000011",
        "1100111",
        "1101111",
        "1101111",
    ]

    start_i, start_j = find_starting_point(matrix)

    if start_i is None and start_j is None:
        raise RuntimeError("Start has not been found!")

    # NOTE: Contains all exit paths which have been found as a list of lists of tuples which represent coordinates.
    exit_paths: list[list[tuple]] = []

    compute_exit_paths(start_i, start_j, [], set(), exit_paths, matrix)
    pprint(exit_paths)


if __name__ == "__main__":
    main()
