def solve():
    original = input()
    modified = input()

    mapping = {}

    for char in modified:
        if char not in mapping:
            mapping[char] = 0
        mapping[char] += 1

    for char in original:
        # NOTE: Every char must be in mapping.
        mapping[char] -= 1

    for char, value in mapping.items():
        if value > 0:
            return char


if __name__ == "__main__":
    print(solve())
