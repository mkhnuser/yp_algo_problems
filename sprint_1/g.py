def solve():
    number_base_ten = int(input())
    remainders = []

    if number_base_ten == 0:
        return 0

    # NOTE: 5.
    # 1. number_base_ten = 2, remainder = 1.
    # 2. number_base_ten = 1, remainder = 0.
    # 3. number_base_ten = 0, remainder = 1.
    while number_base_ten > 0:
        number_base_ten, remainder = divmod(number_base_ten, 2)
        remainders.append(remainder)

    remainders.reverse()
    return "".join(map(str, remainders))


if __name__ == "__main__":
    print(solve())
