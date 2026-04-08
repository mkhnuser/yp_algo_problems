def find_pattern_occurrence(sequence, pattern, start):
    if len(sequence) < len(pattern):
        return -1

    for pos in range(start, len(sequence) - len(pattern) + 1):
        match = True
        c = 0
        for shift in range(len(pattern)):
            s = sequence[pos + shift]
            p = pattern[shift]

            if shift == 0:
                c = abs(s - p)
                continue

            if abs(s - p) != c:
                match = False
                break

        if match:
            return pos

    return -1


def find_all_pattern_occurrences(sequence, pattern):
    occurrences = []
    start = 0
    while True:
        occurrence = find_pattern_occurrence(sequence, pattern, start)
        if occurrence == -1:
            break
        occurrences.append(occurrence)
        start = occurrence + 1
    return occurrences


def solve():
    n = int(input())
    sequence = tuple(map(int, input().split()))
    m = int(input())
    pattern = tuple(map(int, input().split()))

    res = find_all_pattern_occurrences(sequence, pattern)
    return " ".join(map(str, (r + 1 for r in res)))


if __name__ == "__main__":
    print(solve())
