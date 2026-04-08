import sys


def solve_iter():
    string = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())

    words = [
        (word, int(pos))
        for _ in range(n)
        for word, pos in (sys.stdin.readline().strip().split(" "),)
    ]
    words.sort(key=lambda pair: pair[-1])

    i = 0
    j = 0
    word, pos = words[j]

    while i <= len(string):
        if i != pos:
            if i != len(string):
                print(string[i], end="")
            # NOTE: We iterate to the len(string) inclusively.
            # If a user has not requested anything to be inserted "before" the last position, do nothing.
        else:
            print(word, end="")

            if i == len(string):
                # NOTE: The word has been insert at the last position, there are no more words, so just terminate.
                break

            print(string[i], end="")

            j += 1
            if j < len(words):
                word, pos = words[j]

        i += 1

    print("")


def solve_by_sorting():
    string = sys.stdin.readline()
    n = int(sys.stdin.readline())

    words = [
        (word, int(pos))
        for _ in range(n)
        for word, pos in (sys.stdin.readline().split(" "),)
    ]
    words.sort(key=lambda pair: pair[-1], reverse=True)

    # NOTE: Insert "before" position at `pos`.
    for word, pos in words:
        string = string[0:pos] + word + string[pos:]

    return string


if __name__ == "__main__":
    solve_iter()
