import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root):
    return find_max_in_binary_tree(root, root.value)


def find_max_in_binary_tree(node, maximum):
    if node is None:
        return float("-inf")

    if node.value > maximum:
        maximum = node.value

    left_max = find_max_in_binary_tree(node.left, maximum)
    right_max = find_max_in_binary_tree(node.right, maximum)

    return max(left_max, maximum, right_max)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == "__main__":
    test()
