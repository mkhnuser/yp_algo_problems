def solve():
    a = int(input())
    m = int(input())
    s = input()

    hash = 0

    for char in s:
        hash = (hash * a + ord(char)) % m

    return hash


if __name__ == "__main__":
    print(solve())
