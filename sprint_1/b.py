# NOTE: https://contest.yandex.ru/contest/22449/problems/B/.


def solve():
    a, b, c = map(int, input().strip().split(" "))

    remainder = a % 2

    for num in (b, c):
        if num % 2 != remainder:
            return "FAIL"

    return "WIN"


if __name__ == "__main__":
    print(solve())
