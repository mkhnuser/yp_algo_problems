class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class Q:
    def __init__(self):
        self.head = None
        self.tail = None
        self.q_size = 0

    def put(self, x):
        prev_tail = self.tail
        node = Node(value=x)

        if prev_tail is None:
            # NOTE: The queue is empty.
            self.head = node
            self.tail = node
        else:
            # NOTE: There was something in the queue.
            self.tail = node
            prev_tail.next = node

        self.q_size += 1

    def get(self):
        if self.q_size <= 0:
            raise Exception("Queue is empty.")

        head = self.head

        if head == self.tail:
            # NOTE: Reset the queue to the initial state.
            self.tail = None

        self.head = head.next
        self.q_size -= 1
        return head

    def size(self):
        return self.q_size


def test_q():
    q = Q()

    q.put(1)
    assert q.size() == 1
    assert q.get().value == 1
    assert q.size() == 0
    q.put(1)
    q.put(2)
    q.put(3)
    assert q.size() == 3
    assert q.get().value == 1
    assert q.get().value == 2
    assert q.get().value == 3
    assert q.size() == 0

    try:
        q.get()
    except Exception:
        print("Expected exception.")

    assert q.size() == 0
    q.put(1)
    assert q.size() == 1
    assert q.get().value == 1
    assert q.size() == 0


def solve():
    n = int(input())
    q = Q()

    for _ in range(n):
        command = input()
        if command.startswith("get"):
            try:
                print(q.get().value)
            except Exception:
                print("error")
        elif command.startswith("put"):
            __, x = command.split()
            q.put(x)
        elif command.startswith("size"):
            print(q.size())
        else:
            raise RuntimeError("Invalid Command has been received!")


if __name__ == "__main__":
    solve()
