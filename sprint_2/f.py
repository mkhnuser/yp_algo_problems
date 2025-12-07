class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.items:
            return "error"

        return self.items.pop()

    def get_max(self):
        if not self.items:
            return "None"
        return max(self.items)


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
        elif command.startswith("get_max"):
            print(stack.get_max())
        else:
            raise RuntimeError("Invalid Command!")


if __name__ == "__main__":
    solve()
