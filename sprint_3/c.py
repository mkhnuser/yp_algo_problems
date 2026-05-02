def solve():
    sub_string = input()
    main_string = input()

    i = 0
    j = 0

    while i < len(sub_string) and j < len(main_string):
        sub_string_char = sub_string[i]
        main_string_char = main_string[j]

        if main_string_char == sub_string_char:
            i += 1

        j += 1

    return i >= len(sub_string)


if __name__ == "__main__":
    print(solve())
