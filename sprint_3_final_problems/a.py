# https://contest.yandex.ru/contest/23815/run-report/154860771/
#
# --- ПРИНЦИП РАБОТЫ
# Алгоритм является модификацией классического бинарного поиска.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# O(logn), где n - длина массива чисел.
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(n), где n - длина стека вызовов.


def broken_search(nums, target) -> int:
    return recurse_broken_search(nums, target, 0, len(nums) - 1)


def recurse_broken_search(nums, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2
    candidate = nums[middle]
    left_number = nums[left]
    right_number = nums[right]

    if candidate == target:
        return middle

    if left_number <= candidate:
        if target < candidate and target >= left_number:
            # NOTE: left_number <= candidate and target < candidate and target >= left_number.
            return recurse_broken_search(nums, target, left, middle - 1)
        else:
            # NOTE: left_number <= candidate and (target >= candidate or target < left_number).
            return recurse_broken_search(nums, target, middle + 1, right)
    else:
        if target > candidate and target <= right_number:
            # NOTE: left_number > candidate and target > candidate and target <= right_number.
            return recurse_broken_search(nums, target, middle + 1, right)
        else:
            # NOTE: left_number > candidate and (target <= candidate or target > right_number).
            return recurse_broken_search(nums, target, left, middle - 1)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
