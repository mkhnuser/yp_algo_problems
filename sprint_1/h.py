def obtain_number_from_its_representation(digits: list[int], base: int) -> int:
    """Obtain a number from its representation in a particular base."""

    # NOTE: Python will represent a number in base 10 by default,
    # But the main point is that a NUMBER AS SUCH can be obtained.
    addants = []

    n = 0
    for i in reversed(range(0, len(digits))):
        addants.append(digits[i] * (base**n))
        n += 1

    return sum(addants)


def obtain_number_representation(number: int, base: int) -> str:
    """Obtain a number representation in a particular base."""

    if number == 0:
        return "0"

    remainders = []

    while number > 0:
        number, remainder = divmod(number, base)
        remainders.append(remainder)

    remainders.reverse()
    return "".join(map(str, remainders))


def add_two_binary_numbers():
    bin_number_one = input()  # NOTE: base-2.
    bin_number_two = input()  # NOTE: base-2.

    true_mathematical_number_one = obtain_number_from_its_representation(
        list(map(int, bin_number_one)),
        2,
    )
    true_mathematical_number_two = obtain_number_from_its_representation(
        list(map(int, bin_number_two)),
        2,
    )

    result = true_mathematical_number_one + true_mathematical_number_two

    return obtain_number_representation(result, 2)


if __name__ == "__main__":
    print(add_two_binary_numbers())
