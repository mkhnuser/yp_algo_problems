import itertools as it


def solve():
    mapping = {
        "2": {"a", "b", "c"},
        "3": {"d", "e", "f"},
        "4": {"g", "h", "i"},
        "5": {"j", "k", "l"},
        "6": {"m", "n", "o"},
        "7": {"p", "q", "r", "s"},
        "8": {"t", "u", "v"},
        "9": {"w", "x", "y", "z"},
    }
    string = input()

    prod = mapping[string[0]]
    for i in range(len(string) - 1):
        pairs = it.product(prod, mapping[string[i + 1]])
        transformation_genexp = ("".join(tuple_) for tuple_ in pairs)
        prod = transformation_genexp

    res = ["".join(item) for item in prod]
    res.sort()
    return " ".join(res)


if __name__ == "__main__":
    print(solve())
