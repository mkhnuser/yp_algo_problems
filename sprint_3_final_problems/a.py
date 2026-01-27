# https://contest.yandex.ru/contest/23815/run-report/154860771/
#
# --- ПРИНЦИП РАБОТЫ
# Алгоритм является модификацией классического рекурсивного бинарного поиска.
# Основная сложность: мы должны правильно отсекать половину массива.
#
#
#
# Для этого мы вначале проверяем, какая часть массива, левая или правая, отсортирована от меньшего к большему;
# для этого используется первый if-блок. Данная проверка необходима для следующего вложенного шага алгоритма,
# когда мы находим интервал, в рамках которого лежит наш target.
#
# Иными словами, для того, чтобы гарантировать, что, например, проверка:
#
#   target >= candidate or target < left_number
#
# имеет смысл, мы должны гарантировать, что left_number <= candidate.
#
#
#
# В противном случае, если left_number > candidate, то условие:
#
#   target >= candidate or target < left_number
#
# всё равно может выполнятся для, например:
#
#   left_number = 10, candidate = 1, target = 18
#
# и тогда мы отсечём левую часть массива, в которой может быть target.
#
# Рассуждения для правой части массива аналогичны.
#
#
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
