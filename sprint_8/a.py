def solve():
    words = input().strip()
    strings = words.split()
    strings.reverse()
    return " ".join(strings)


if __name__ == "__main__":
    print(solve())
