import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    return find_depth(root)


def find_depth(node):
    if node is None:
        return 0

    left_depth = find_depth(node.left)
    right_depth = find_depth(node.right)
    return max(left_depth, right_depth) + 1


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5) == 3


if __name__ == "__main__":
    test()
