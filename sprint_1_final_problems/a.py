# https://contest.yandex.ru/contest/22450/run-report/152689550/


def compute_distance_from_left_to_right(n, input_list, output_list):
    the_last_left_zero_index = None
    for i in range(0, n):
        current_element = input_list[i]

        if current_element == 0:
            the_last_left_zero_index = i
            output_list[i] = 0
        elif current_element != 0 and the_last_left_zero_index is not None:
            output_list[i] = i - the_last_left_zero_index
        elif current_element != 0 and the_last_left_zero_index is None:
            output_list[i] = float("+inf")


def compute_distance_from_right_to_left(n, input_list, output_list):
    the_last_right_zero_index = None
    for i in reversed(range(0, n)):
        current_element = input_list[i]

        if current_element == 0:
            the_last_right_zero_index = i
            output_list[i] = 0
        elif current_element != 0 and the_last_right_zero_index is not None:
            distance = the_last_right_zero_index - i
            previously_computed_distance = output_list[i]
            if distance < previously_computed_distance:
                output_list[i] = distance


def computer_distance_to_the_nearest_zeros():
    n = int(input())
    input_list = list(map(int, input().split()))
    output_list = [0.0 for _ in range(n)]

    compute_distance_from_left_to_right(n, input_list, output_list)
    compute_distance_from_right_to_left(n, input_list, output_list)

    return " ".join(map(str, output_list))


if __name__ == "__main__":
    print(computer_distance_to_the_nearest_zeros())
