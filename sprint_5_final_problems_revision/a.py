import math


class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, element):
        self.data.append(element)
        self._sift_up(len(self.data) - 1)

    def delete(self):
        if not self.data:
            return None

        self.data[0], self.data[len(self.data) - 1] = (
            self.data[len(self.data) - 1],
            self.data[0],
        )
        out = self.data.pop()
        self._sift_down(0)
        return out

    def _get_left_child_index(self, index):
        return 2 * index + 1

    def _get_right_child_index(self, index):
        return 2 * index + 2

    def _get_parent_index(self, index):
        return math.floor((index - 1) / 2)

    def _sift_down(self, index):
        if index >= len(self.data):
            return

        smallest_i = index
        left_i = self._get_left_child_index(index)
        right_i = self._get_right_child_index(index)

        if left_i < len(self.data) and self.data[left_i] < self.data[smallest_i]:
            smallest_i = left_i
        if right_i < len(self.data) and self.data[right_i] < self.data[smallest_i]:
            smallest_i = right_i

        if smallest_i != index:
            self.data[smallest_i], self.data[index] = (
                self.data[smallest_i],
                self.data[index],
            )
            self._sift_down(smallest_i)

    def _sift_up(self, index):
        if index <= 0:
            return

        parent_index = self._get_parent_index(index)
        parent_value = self.data[parent_index]
        current_value = self.data[index]

        if current_value < parent_value:
            self.data[index], self.data[parent_index] = (
                self.data[parent_index],
                self.data[index],
            )
            self._sift_up(parent_index)


def build_heap(array, heap):
    for el in array:
        heap.insert(el)


def solve():
    n = int(input())
    array = []
    heap = MinHeap()

    for _ in range(n):
        string = input()
        login, num_of_solved_problems, penalty = string.split()
        num_of_solved_problems = -int(num_of_solved_problems)
        penalty = int(penalty)
        array.append((num_of_solved_problems, penalty, login))

    build_heap(array, heap)
    output = []

    while (tp := heap.delete()) is not None:
        output.append((tp[-1]))

    # NOTE: Does not work.
    for o in output:
        print(o)


if __name__ == "__main__":
    solve()
