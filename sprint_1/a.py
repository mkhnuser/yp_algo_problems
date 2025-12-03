# NOTE: https://contest.yandex.ru/contest/22449/problems/A/.


def solve():
    a, x, b, c = map(int, input().strip().split(" "))
    return a * (x**2) + b * x + c


if __name__ == "__main__":
    print(solve())
