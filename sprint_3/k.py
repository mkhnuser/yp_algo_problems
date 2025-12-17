def merge(arr, lf, mid, rg):
    left_part = arr[lf:mid]
    right_part = arr[mid:rg]

    res = [None] * (rg - lf)

    left_index = 0
    right_index = 0
    res_index = 0

    while left_index < (mid - lf) and right_index < (rg - mid):
        left_el = left_part[left_index]
        right_el = right_part[right_index]

        if left_el <= right_el:
            left_index += 1
            res[res_index] = left_el
        else:
            right_index += 1
            res[res_index] = right_el

        res_index += 1

    while left_index < (mid - lf):
        res[res_index] = left_part[left_index]
        left_index += 1
        res_index += 1

    while right_index < (rg - mid):
        res[res_index] = right_part[right_index]
        right_index += 1
        res_index += 1

    return res


def merge_sort(arr, lf, rg):
    if (rg - lf) == 0 or (rg - lf) == 1:
        return arr

    sorted_left_part = merge_sort(arr, lf, (rg + lf) // 2)
    sorted_right_part = merge_sort(arr, (rg + lf) // 2, rg)

    arr[lf:rg] = merge(arr, lf, (rg + lf) // 2, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == "__main__":
    test()
