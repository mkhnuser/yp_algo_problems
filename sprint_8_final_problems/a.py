# https://contest.yandex.ru/contest/26133/run-report/160078732/
#
# --- ПРИНЦИП РАБОТЫ
# Распакуем каждую из строк, следуя описанию задачи.
#
# После этого, итеративно будем искать общий префикс двух строк,
# поэтапно "отрезая" последний символ, пока это возможно.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# O(k * n), где k - кол-во строк, а n - длина самой большой из них.
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(n), где n - длина большей из строк.


def transform_prefix(str_):
    multiples = []
    chars = []
    result = []

    for char in str_:
        if char.isnumeric():
            multiples.append(int(char))
            continue

        if char == "[":
            chars.append([])
            continue

        if char == "]":
            if len(chars) == 1:
                prev_char = chars.pop()
                prev_multiple = multiples.pop()
                result.append("".join(prev_char) * prev_multiple)
                continue

            prev_char = chars.pop()
            prev_multiple = multiples.pop()
            prev = "".join(prev_char)
            chars[-1].append(prev * prev_multiple)
            continue

        if len(chars) == 0:
            result.append(char)
            continue

        chars[-1].append(char)

    result_string = "".join(result)
    return result_string


def find_packed_prefix(n):
    if n == 0:
        return ""

    first_prefix = transform_prefix(input())

    for _ in range(n - 1):
        str_ = transform_prefix(input())

        while str_[: len(first_prefix)] != first_prefix and first_prefix != "":
            first_prefix = first_prefix[:-1]

    return first_prefix


def solve():
    n = int(input())
    return find_packed_prefix(n)


if __name__ == "__main__":
    print(solve())
