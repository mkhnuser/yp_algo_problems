def solve():
    n = int(input())
    strings = (input() for _ in range(n))

    prefix_length = 0
    for chars in zip(*strings):
        if not len(set(chars)) == 1:
            break
        prefix_length += 1

    return prefix_length


if __name__ == "__main__":
    print(solve())
