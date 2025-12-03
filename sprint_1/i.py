def solve():
    number = int(input())
    powers_of_four = {4**i for i in range(0, 10)}
    return number in powers_of_four


if __name__ == "__main__":
    print(solve())
