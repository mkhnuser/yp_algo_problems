def solve():
    n = int(input())
    mapping = {}

    for _ in range(n):
        circle_name = input()
        mapping[circle_name] = None

    for key in mapping:
        print(key)


if __name__ == "__main__":
    solve()
