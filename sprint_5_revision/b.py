import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    return recurse(root)


def recurse(node):
    to_be_visited = []
    to_be_visited.append(node)

    while to_be_visited:
        v = to_be_visited.pop()

        if v is None:
            continue

        if abs(find_height(v.left) - find_height(v.right)) > 1:
            return False

        to_be_visited.append(v.left)
        to_be_visited.append(v.right)

    return True


def find_height(node):
    if node is None:
        return -1

    left_height = find_height(node.left)
    right_height = find_height(node.right)
    return 1 + max(left_height, right_height)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


def test_height():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert find_height(node5) == 2


if __name__ == "__main__":
    test()
