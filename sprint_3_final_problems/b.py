# https://contest.yandex.ru/contest/23815/run-report/154995461/
#
# --- ПРИНЦИП РАБОТЫ
# Алгоритм является in-place-реализацией quick sort.
# Мы рандомизируем выбор пивота для того, чтобы не иметь квадратичную сложность для массивов вида [1, 2, 3, 4, 5, 6, 7].
# На каждой рекурсивной итерации алгоритма мы поддерживаем инвариант, что все элементы больше пивота будут после него, а все элементы меньше - до него.
# Мы поддерживаем этот инвариант путём итерации с обоих концов и делая swap элементов, если они нарушают инвариант.
# После этого мы рекурсивно сортируем оставшиеся части массива.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# O(nlogn), где n - длина массива чисел.
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(1).


import random


def solve():
    data = []
    n = int(input())
    for _ in range(n):
        login, problem_count, penalty = input().split()
        data.append(
            (
                -int(problem_count),
                int(penalty),
                login,
            )
        )

    sort_in_place_using_quick_sort(data, 0, len(data) - 1)

    return data


def sort_in_place_using_quick_sort(array, left_index, right_index):
    if left_index >= right_index:
        return array

    pivot_index = random.randint(left_index, right_index)
    array[left_index], array[pivot_index] = array[pivot_index], array[left_index]

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
