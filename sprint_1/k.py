def solve():
    _ = int(input())
    main_number = int(input().replace(" ", ""))
    n = int(input())
    return " ".join(str(main_number + n))


if __name__ == "__main__":
    print(solve())
