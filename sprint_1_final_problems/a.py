# https://contest.yandex.ru/contest/22450/run-report/152962733/


def go_left_to_right(n, input_list, output_list):
    last_zero_index = None
    for i in range(0, n):
        current = input_list[i]

        if current == 0:
            last_zero_index = i
            output_list[i] = 0
        elif current != 0 and last_zero_index is not None:
            output_list[i] = i - last_zero_index
        elif current != 0 and last_zero_index is None:
            output_list[i] = float("+inf")


def go_right_to_left(n, input_list, output_list):
    last_zero_index = None
    for i in reversed(range(0, n)):
        current = input_list[i]

        if current == 0:
            last_zero_index = i
            output_list[i] = 0
        elif current != 0 and last_zero_index is not None:
            distance = last_zero_index - i
            prev_distance = output_list[i]
            if distance < prev_distance:
                output_list[i] = distance


def compute_distance_to_zeros():
    n = int(input())
    input_list = list(map(int, input().split()))
    output_list = [0.0] * n

    go_left_to_right(n, input_list, output_list)
    go_right_to_left(n, input_list, output_list)

    return " ".join(map(str, output_list))


if __name__ == "__main__":
    print(compute_distance_to_zeros())
