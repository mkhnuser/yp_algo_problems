def solve():
    num = int(input())
    res = []

    # NOTE: If a number n does not have a divisor less than sqrt(n),
    # Then it does not have a divisor greater than sqrt(n).
    n = 2
    while (n**2) <= num:
        while num % n == 0:
            num /= n
            res.append(int(n))  # NOTE: Convert to int for proper printing.
        n += 1

    # NOTE: Handle a case if THE INITIAL NUMBER num is itself prime
    # Or you've obtained a prime in the step above.
    # For example: 13.
    if num > 1:
        res.append(int(num))  # NOTE: Convert to int for proper printing.

    return " ".join(map(str, res))


if __name__ == "__main__":
    print(solve())
