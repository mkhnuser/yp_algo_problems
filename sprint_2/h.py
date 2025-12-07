def solve():
    string = input()

    if string == "":
        return True

    stack = []

    for char in string:
        if char in ("[", "(", "{"):
            stack.append(char)
        elif char in ("]", ")", "}"):
            if not stack:
                return False
            popped = stack.pop()
            if char == "]" and popped != "[":
                return False
            elif char == ")" and popped != "(":
                return False
            elif char == "}" and popped != "{":
                return False

        else:
            raise RuntimeError("Invalid Char in the string!")

    return len(stack) == 0


if __name__ == "__main__":
    # NOTE: ""
    # "()"
    # "()()"
    # "(())"
    # "(())[]"
    # "(()"
    # "("
    # ")"
    # "([]"
    print(solve())
