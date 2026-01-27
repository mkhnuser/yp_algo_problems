def solve():
    string_one = input()
    string_two = input()

    if len(string_one) != len(string_two):
        return False

    one_to_two_mapping = {}
    two_to_one_mapping = {}

    for char_one, char_two in zip(string_one, string_two):
        if char_one in one_to_two_mapping:
            if one_to_two_mapping[char_one] != char_two:
                return False
        else:
            one_to_two_mapping[char_one] = char_two

        if char_two in two_to_one_mapping:
            if two_to_one_mapping[char_two] != char_one:
                return False
        else:
            two_to_one_mapping[char_two] = char_one

    return True


if __name__ == "__main__":
    print("YES" if solve() else "NO")
