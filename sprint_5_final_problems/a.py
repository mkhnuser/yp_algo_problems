# https://contest.yandex.ru/contest/24810/run-report/157242594/
#
# --- ПРИНЦИП РАБОТЫ
# Классическая реализация максимальной кучи, которая включает в себя:
# поиск индексов левого и правого потомка, просеивание вниз, построение максимальной кучи и сортировку.
#
# Отедельное внимание стоит уделить тому, что мы используем унарный минус перед количеством решенных задач,
# что позволяет нам сортировать входной массив от меньшего к большему так, как этого требует условие задачи.
# ЯП Пайтон также помогает нам лаконично сравнимать между собой кортежи, сравнивая элементы слева направо.
#
# Сортировка происходит in-place.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# O(n * logn), где n - количество элементов. Действительно, мы итерируемся по n элементов и в рамках
# каждой итерации вызываем sift_down-рутину, которая работает за O(log n) (высота кучи).
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(1) - так как не требуется дополнительного места, т.к. сортировка in-place.


class MaxHeap:
    def __init__(self, data: list[tuple[int, int, str]]) -> None:
        self.data = data
        self.length = len(data)

    def get_left_child_index(self, i):
        return 2 * i + 1

    def get_right_child_index(self, i):
        return 2 * i + 2

    def sift_down(self, i: int) -> None:
        L = self.get_left_child_index(i)
        R = self.get_right_child_index(i)
        current_value = self.data[i]

        if L < self.length and self.data[L] > current_value:
            largest_index = L
        else:
            largest_index = i

        if R < self.length and self.data[R] > self.data[largest_index]:
            largest_index = R

        if largest_index != i:
            self.data[largest_index], self.data[i] = (
                self.data[i],
                self.data[largest_index],
            )
            self.sift_down(largest_index)

    def build_max_heap(self) -> None:
        for i in range(self.length // 2, -1, -1):
            self.sift_down(i)

    def heap_sort(self) -> None:
        self.build_max_heap()

        for i in range(self.length - 1, 0, -1):
            self.data[0], self.data[i] = self.data[i], self.data[0]
            self.length -= 1
            self.sift_down(0)


def solve():
    n = int(input())

    participants = []
    for _ in range(n):
        login, number_of_solved_problems, penalty = input().split()
        participants.append(
            (
                -int(number_of_solved_problems),
                int(penalty),
                login,
            )
        )

    max_heap = MaxHeap(participants)
    max_heap.heap_sort()

    for participant in participants:
        print(participant[2])


if __name__ == "__main__":
    solve()
