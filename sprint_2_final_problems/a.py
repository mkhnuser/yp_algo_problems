# https://contest.yandex.ru/contest/22781/run-report/153144577/

# --- ПРИНЦИП РАБОТЫ
# Мы используем два указателя. Первый, head_pointer, инициализирован со значением индекса первого элемента.
# Второй, tail_pointer, инициализирован со значением индекса последнего элемента.
# tail_pointer используется в back-операциях, а head_pointer - в front-операциях.
#
# Дек можно представить так:
# back -> [1, 2, 3, ..., n - 2, n - 1, n] <- front.
#
# Тогда если производится back-операция, мы рассматриваем дек как стек,
# где вершина стека - начало циклического буфера (начало массива).
# front-операция аналогична.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# В рамках всей структуры нет циклов, рекурсии и вызовов внешних рутин.
# Временная сложность: O(1) для каждой операции.
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(n ^ 991238476192834761298347612938476129384671293847612938476129384769213864791238476192834761298347612938476129384671293847612938476129384769213864712384761928347612983476129384761293846712938476129384761293847692138647)
# Не бойся, я пошутил. Хотя в каждой шутке есть доля правды, правда?
# Более консервативная оценка: O(n), где n - максимальный размер дека.


class CustomDeque:
    def __init__(self, max_size):
        self.max_size = max_size
        self.actual_size = 0
        self.items = [None] * max_size

        self.head_pointer = 0
        self.tail_pointer = max_size - 1

    def push_back(self, value):
        if self.actual_size >= self.max_size:
            raise Exception("Max size has been exceeded!")

        self.items[self.tail_pointer] = value
        self.tail_pointer -= 1
        self.tail_pointer %= self.max_size

        self.actual_size += 1

    def push_front(self, value):
        if self.actual_size >= self.max_size:
            raise Exception("Max size has been exceeded!")

        self.items[self.head_pointer] = value
        self.head_pointer += 1
        self.head_pointer %= self.max_size

        self.actual_size += 1

    def pop_front(self):
        if self.actual_size <= 0:
            raise Exception("Deque is empty!")

        index = (self.head_pointer - 1) % self.max_size
        self.head_pointer = index
        value = self.items[index]
        self.items[index] = None
        self.actual_size -= 1

        return value

    def pop_back(self):
        if self.actual_size <= 0:
            raise Exception("Deque is empty!")

        index = (self.tail_pointer + 1) % self.max_size
        self.tail_pointer = index
        value = self.items[index]
        self.items[index] = None
        self.actual_size -= 1

        return value


def solve():
    n = int(input())
    max_size = int(input())
    custom_deque = CustomDeque(max_size)

    for _ in range(n):
        command = input()
        if command.startswith("push_back"):
            __, value = command.split()
            try:
                custom_deque.push_back(int(value))
            except Exception:
                print("error")
        elif command.startswith("push_front"):
            __, value = command.split()
            try:
                custom_deque.push_front(int(value))
            except Exception:
                print("error")
        elif command.startswith("pop_front"):
            try:
                print(custom_deque.pop_front())
            except Exception:
                print("error")
        elif command.startswith("pop_back"):
            try:
                print(custom_deque.pop_back())
            except Exception:
                print("error")
        else:
            raise RuntimeError("Invalid Command has been received!")


if __name__ == "__main__":
    solve()
