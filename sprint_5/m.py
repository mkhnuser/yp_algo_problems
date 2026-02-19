def get_parent_index(i):
    return i // 2


def sift_up(A, i) -> int:
    p = get_parent_index(i)

    if p == 0:
        return i

    parent_value = A[p]
    current_value = A[i]

    if parent_value < current_value:
        A[p], A[i] = A[i], A[p]
        return sift_up(A, p)

    return i


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == "__main__":
    test()
