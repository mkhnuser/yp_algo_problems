# NOTE: https://contest.yandex.ru/contest/22449/problems/F/.


def solve():
    sentence = input().strip().lower()
    transformed_sentence = "".join(filter(str.isalnum, (s for s in sentence)))

    left = 0
    right = len(transformed_sentence) - 1

    while left < right:
        left_char = transformed_sentence[left]
        right_char = transformed_sentence[right]

        if left_char != right_char:
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(solve())
