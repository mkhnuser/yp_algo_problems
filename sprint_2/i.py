class MyQueueSized:
    def __init__(self, max_size):
        self.sentinel = object()
        self.enqueue_pointer = max_size - 1
        self.dequeue_pointer = max_size - 1

        self.max_size = max_size
        self.items_size = 0

        self.items = [self.sentinel for _ in range(max_size)]

    def push(self, x):
        if self.items_size >= self.max_size:
            raise Exception("Max size has been exceeded!")

        self.items[self.enqueue_pointer] = x
        self.enqueue_pointer -= 1
        self.enqueue_pointer %= self.max_size
        self.items_size += 1

    def pop(self):
        if not self.items_size:
            raise Exception("No items!")

        item = self.items[self.dequeue_pointer]
        self.dequeue_pointer -= 1
        self.dequeue_pointer %= self.max_size
        self.items_size -= 1
        return item

    def peek(self):
        if not self.items_size:
            raise Exception("No items!")

        return self.items[self.dequeue_pointer]

    def size(self):
        return self.items_size


def solve():
    n = int(input())
    max_size = int(input())
    q = MyQueueSized(max_size)

    for _ in range(n):
        command = input()
        if command.startswith("peek"):
            try:
                print(q.peek())
            except Exception:
                print("None")
        elif command.startswith("push"):
            __, x = command.split()
            try:
                q.push(x)
            except Exception:
                print("error")
        elif command.startswith("pop"):
            try:
                print(q.pop())
            except Exception:
                print("None")
        elif command.startswith("size"):
            print(q.size())
        else:
            raise RuntimeError("Invalid command has been received!")


if __name__ == "__main__":
    solve()
