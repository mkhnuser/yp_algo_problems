# https://contest.yandex.ru/contest/22450/run-report/152901860/


def obtain_maximum_element(matrix):
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


def get_count():
    k = int(input())
    matrix = []
    number_of_rows = 4

    for _ in range(number_of_rows):
        row = list(input())
        row = [int(char) if str.isnumeric(char) else char for char in row]
        matrix.append(row)

    maximum_numeric = obtain_maximum_element(matrix)

    counter = 0
    max_keypresses = k * 2

    for t in range(1, maximum_numeric + 1):
        number_of_numbers = obtain_number_of_numbers(matrix, t)

        if not number_of_numbers:
            continue

        if max_keypresses >= number_of_numbers:
            counter += 1

    return counter


if __name__ == "__main__":
    print(get_count())
