class Stack:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, x):
        self.items.append(x)

        if not self.max_items or self.max_items[-1] <= x:
            self.max_items.append(x)

    def pop(self):
        if not self.items:
            return "error"

        popped = self.items.pop()

        if self.max_items[-1] == popped:
            self.max_items.pop()

        return popped

    def get_max(self):
        if not self.max_items:
            return "None"
        return self.max_items[-1]

    def top(self):
        if not self.items:
            return "error"
        return self.items[-1]


def solve():
    stack = Stack()
    n = int(input())

    for _ in range(n):
        command = input()

        if command.startswith("push"):
            __, number_str = command.split()
            stack.push(int(number_str))
        elif command.startswith("pop"):
            res = stack.pop()
            if res == "error":
                print("error")
        elif command.startswith("top"):
            print(stack.top())
        elif command.startswith("get_max"):
            print(stack.get_max())
        else:
            raise RuntimeError("Invalid Command!")


if __name__ == "__main__":
    solve()
