def solve():
    res = []
    n = int(input())

    def gen_parenthesis(prefix, num_of_open, num_of_close):
        if len(prefix) == 2 * n:
            res.append(prefix)
            return

        if num_of_open < n:
            gen_parenthesis(prefix + "(", num_of_open + 1, num_of_close)

        if num_of_close < num_of_open:
            gen_parenthesis(prefix + ")", num_of_open, num_of_close + 1)

    gen_parenthesis("", 0, 0)
    return res


if __name__ == "__main__":
    for pair in solve():
        print(pair)
