def solve():
    num_of_rows = int(input())
    num_of_columns = int(input())

    matrix = []
    for _ in range(num_of_rows):
        row = input().split()
        matrix.append(row)

    output_matrix = [[None for _ in range(num_of_rows)] for __ in range(num_of_columns)]

    for i in range(num_of_rows):
        for j in range(num_of_columns):
            output_matrix[j][i] = matrix[i][j]

    return output_matrix


if __name__ == "__main__":
    result_matrix = solve()
    for row in result_matrix:
        print(" ".join(row))
