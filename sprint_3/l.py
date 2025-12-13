# https://contest.yandex.ru/contest/23638/problems/L/#3484683/2020_11_16/hIKAEB0ETO


def find_day_numbers(savings, s, left_index, right_index, days):
    if left_index > right_index:
        if not days:
            return -1
        return days[-1]

    middle_index = (left_index + right_index) // 2
    el = savings[middle_index]

    if el >= s:
        # TODO: Go left.
        days.append(middle_index)
        right_index = middle_index - 1
        return find_day_numbers(savings, s, left_index, right_index, days)
    else:
        # TODO: Go right since el < s.
        left_index = middle_index + 1
        return find_day_numbers(savings, s, left_index, right_index, days)


def solve() -> str:
    n = int(input())
    savings = list(map(int, input().split()))
    s = int(input())

    day_one_index = find_day_numbers(
        savings,
        s,
        left_index=0,
        right_index=len(savings) - 1,
        days=[],
    )

    if day_one_index == -1:
        return "-1 -1"

    day_two_index = find_day_numbers(
        savings,
        s * 2,
        left_index=day_one_index,
        right_index=len(savings) - 1,
        days=[],
    )

    if day_two_index == -1:
        day_two_index = -2

    return " ".join(map(str, (day_one_index + 1, day_two_index + 1)))


if __name__ == "__main__":
    print(solve())
