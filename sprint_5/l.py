def sift_down(heap, idx) -> int:
    index = idx
    return recurse_sift_down(heap, index)


def get_left_child_index(index):
    return 2 * index


def get_right_child_index(index):
    return (2 * index) + 1


def recurse_sift_down(heap, index) -> int:
    largest_i = index
    left_i = get_left_child_index(index)
    right_i = get_right_child_index(index)

    if left_i < len(heap) and heap[left_i] > heap[largest_i]:
        largest_i = left_i
    if right_i < len(heap) and heap[right_i] > heap[largest_i]:
        largest_i = right_i

    if largest_i != index:
        heap[index], heap[largest_i] = heap[largest_i], heap[index]
        return recurse_sift_down(heap, largest_i)

    return index


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == "__main__":
    test()
