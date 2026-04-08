from collections import Counter


def solve():
    # NOTE: This solution does not work for some reason.
    n = int(input())
    strings = [input() for _ in range(n)]
    counter = Counter(strings)
    return sorted(counter.most_common(None), key=lambda pair: len(pair[0]))[0][0]


if __name__ == "__main__":
    print(solve())
