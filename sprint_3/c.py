def solve():
    sub = input()
    string = input()

    i = 0
    j = 0

    while j < len(string) and i < len(sub):
        main_char = string[j]
        sub_char = sub[i]

        if sub_char == main_char:
            i += 1

        j += 1

    return i >= len(sub)


if __name__ == "__main__":
    print(solve())
