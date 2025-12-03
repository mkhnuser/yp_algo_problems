# NOTE: https://contest.yandex.ru/contest/22449/problems/E/.


def solve():
    L = int(input())
    sentence = input().strip()
    sentence += " "

    left = 0
    right = 0

    global_max = 0
    global_left = 0
    global_right = 0

    for i in range(len(sentence)):
        current_symbol = sentence[i]

        if current_symbol == " ":
            current_max = right - left
            if current_max > global_max:
                global_max = current_max
                global_left = left
                global_right = right - 1

            left = i + 1
            right = i + 1
        else:
            right += 1

    return (sentence[global_left : global_right + 1], global_max)


if __name__ == "__main__":
    for ans in solve():
        print(ans)
