def solve():
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    input_string = input()
    output = []
    recurse_solution(
        input_string, "", mapping, output, terminator_length=len(input_string)
    )
    return output


def recurse_solution(input_string, current_string, mapping, output, terminator_length):
    if len(current_string) == terminator_length:
        output.append(current_string)
        return

    for i in range(len(input_string)):
        for current_char in mapping[input_string[i]]:
            recurse_solution(
                input_string[i + 1 :],
                current_string + current_char,
                mapping,
                output,
                terminator_length,
            )


if __name__ == "__main__":
    print(*solve())
