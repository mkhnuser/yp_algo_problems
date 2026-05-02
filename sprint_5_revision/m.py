import math


def sift_up(heap, idx) -> int:
    return recurse_sift_up(heap, idx)


def get_parent_index(index):
    return math.floor((index) / 2)


def recurse_sift_up(heap, index):
    if index == 1:
        return index

    parent_index = get_parent_index(index)
    parent_value = heap[parent_index]
    current_value = heap[index]

    if current_value > parent_value:
        heap[index] = parent_value
        heap[parent_index] = current_value
        index = recurse_sift_up(heap, parent_index)

    return index


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == "__main__":
    test()
