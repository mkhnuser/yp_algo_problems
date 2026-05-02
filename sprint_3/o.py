def solve():
    n = int(input())
    list_ = list(map(int, input().split()))
    k = int(input())

    area_differences = []

    for i in range(len(list_) - 1):
        first_area = list_[i]
        for j in range(i + 1, len(list_)):
            second_area = list_[j]
            area_differences.append(abs(first_area - second_area))

    area_differences.sort()
    return area_differences[k - 1]


if __name__ == "__main__":
    print(solve())
