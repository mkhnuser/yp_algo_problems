import string


def solve():
    alphabet = string.ascii_lowercase
    letters = {letter for i, letter in enumerate(alphabet, start=1) if i % 2 == 0}
    a = input()
    b = input()

    a_order = []
    for char in a:
        if char not in letters:
            continue
        a_order.append(char)

    b_order = []
    for char in b:
        if char not in letters:
            continue
        b_order.append(char)

    a = "".join(a_order)
    b = "".join(b_order)

    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1


if __name__ == "__main__":
    print(solve())
