def solve():
    _ = input()
    numbers = map(int, input().split())
    range_ = [0] * 3

    for num in numbers:
        range_[num] += 1

    output = []

    for i in range(len(range_)):
        output.extend([i] * range_[i])

    return map(str, output)


if __name__ == "__main__":
    print(" ".join(solve()))
