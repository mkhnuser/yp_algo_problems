def sift_down(A, i) -> int:
    lefty = get_left_child_index(i)
    righty = get_right_child_index(i)

    if lefty <= len(A) - 1 and A[lefty] > A[i]:
        largest_index = lefty
    else:
        largest_index = i

    if righty <= len(A) - 1 and A[righty] > A[largest_index]:
        largest_index = righty

    if largest_index != i:
        A[i], A[largest_index] = A[largest_index], A[i]
        return sift_down(A, largest_index)
    else:
        return i


def get_left_child_index(i):
    return 2 * i


def get_right_child_index(i):
    return (2 * i) + 1


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    res = sift_down(sample, 2)
    print(res)
    assert res == 5


if __name__ == "__main__":
    test()
