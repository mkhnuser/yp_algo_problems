# NOTE: https://contest.yandex.ru/contest/22449/problems/D/.


def solve():
    n = int(input())
    numbers = list(map(int, input().split(" ")))
    counter = 0

    # NOTE: O(n) time | O(1) space.
    for i in range(n):
        left_day = None
        right_day = None

        if i - 1 >= 0:
            left_day = numbers[i - 1]
        if i + 1 <= (n - 1):
            right_day = numbers[i + 1]

        current_day = numbers[i]

        if left_day is None and right_day is None:
            # NOTE: We have only one day.
            counter += 1
        elif left_day is None and right_day is not None:
            if current_day > right_day:
                counter += 1
        elif left_day is not None and right_day is None:
            if current_day > left_day:
                counter += 1
        elif left_day is not None and right_day is not None:
            if current_day > left_day and current_day > right_day:
                counter += 1
        else:
            raise RuntimeError("Invalid Application State.")

    return counter


if __name__ == "__main__":
    print(solve())
