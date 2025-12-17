from functools import cmp_to_key


def compare_by_concatenation(a, b):
    """Compares by string concatenation."""
    if a + b > b + a:
        # NOTE: a goes before b.
        return -1
    elif a + b < b + a:
        # NOTE: b goes before a.
        return 1
    else:
        return 0


def solve():
    n = int(input())
    numbers = input().split()
    # NOTE: The easies way to use comparison function.
    numbers.sort(key=cmp_to_key(compare_by_concatenation))
    return "".join(numbers)


if __name__ == "__main__":
    print(solve())
