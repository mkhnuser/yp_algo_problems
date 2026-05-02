def solve():
    n = int(input())
    list_ = list(map(int, input().split()))
    k = int(input())

    counter_mapping = {}

    for num in list_:
        if num not in counter_mapping:
            counter_mapping[num] = 0
        counter_mapping[num] += 1

    items = list(counter_mapping.items())
    # NOTE: Sort by: 1) the number of participants DESC, 2) uni number ASC.
    items.sort(key=lambda item: (item[1], -item[0]), reverse=True)

    for item in items[:k]:
        print(item[0], end=" ")
    print()


if __name__ == "__main__":
    solve()
