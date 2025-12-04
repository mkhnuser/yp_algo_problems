# https://contest.yandex.ru/contest/22450/run-report/152697581/


def obtain_maximum_numeric_element_in_a_game_matrix(matrix):
    maximum_numeric = 0

    for row in matrix:
        for alphanum in row:
            if alphanum == ".":
                continue

            num = alphanum
            if num > maximum_numeric:
                maximum_numeric = num

    return maximum_numeric


def obtain_number_of_numbers(matrix, target):
    counter = 0

    for row in matrix:
        for alphanum in row:
            if alphanum == ".":
                continue

            num = alphanum
            if num == target:
                counter += 1

    return counter


def obtain_count():
    k = int(input())
    matrix = []

    # NOTE: O(1).
    for _ in range(4):
        row = list(input())
        row = [int(char) if str.isnumeric(char) else char for char in row]
        matrix.append(row)

    # NOTE: O(1).
    maximum_numeric = obtain_maximum_numeric_element_in_a_game_matrix(matrix)

    counter = 0
    maximum_number_of_allowed_key_presses = k * 2

    # NOTE: O(maximum_numeric).
    for t in range(1, maximum_numeric + 1):
        number_of_numbers = obtain_number_of_numbers(matrix, t)

        if not number_of_numbers:
            continue

        if maximum_number_of_allowed_key_presses >= number_of_numbers:
            counter += 1

    return counter


if __name__ == "__main__":
    print(obtain_count())
