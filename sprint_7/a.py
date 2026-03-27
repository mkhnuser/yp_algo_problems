def solve():
    n = int(input())
    stocks = list(map(int, input().split()))

    margin = 0

    for i in range(0, n - 1):
        if stocks[i] < stocks[i + 1]:
            margin += stocks[i + 1] - stocks[i]

    return margin


if __name__ == "__main__":
    print(solve())
