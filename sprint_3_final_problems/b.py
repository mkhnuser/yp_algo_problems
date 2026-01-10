# https://contest.yandex.ru/contest/23815/run-report/154861547/
#
# --- ПРИНЦИП РАБОТЫ
# Алгоритм является in-place-реализацией quick sort.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# O(nlogn), где n - длина массива чисел.
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(1).


def solve():
    data = []
    n = int(input())
    for _ in range(n):
        login, problem_count, penalty = input().split()
        data.append(
            (
                -int(problem_count),  # NOTE: This is top priority.
                int(penalty),
                login,
            )
        )

    sort_in_place_using_quick_sort(data, 0, len(data) - 1)

    return data


def sort_in_place_using_quick_sort(array, left_index, right_index):
    if left_index >= right_index:
        return array

    pivot = array[left_index]
    left_pointer = left_index + 1
    right_pointer = right_index

    while left_pointer <= right_pointer:
        left_item = array[left_pointer]
        right_item = array[right_pointer]

        if left_item > pivot and right_item < pivot:
            array[left_pointer], array[right_pointer] = (
                array[right_pointer],
                array[left_pointer],
            )
            left_pointer += 1
            right_pointer -= 1
        elif left_item <= pivot:
            left_pointer += 1
        elif right_item >= pivot:
            right_pointer -= 1

    array[left_index], array[right_pointer] = array[right_pointer], array[left_index]

    left_size = (right_pointer - 1) - left_index
    right_size = right_index - (right_pointer + 1)

    if left_size > right_size:
        sort_in_place_using_quick_sort(array, right_pointer + 1, right_index)
        sort_in_place_using_quick_sort(array, left_index, right_pointer - 1)
    else:
        sort_in_place_using_quick_sort(array, left_index, right_pointer - 1)
        sort_in_place_using_quick_sort(array, right_pointer + 1, right_index)

    return array


if __name__ == "__main__":
    for datum in solve():
        print(datum[2])
