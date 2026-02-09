import os


LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"


if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> float:
    return find_maximum_value(root, maximum_value=root.value)


def find_maximum_value(node, maximum_value) -> float:
    if node is None:
        return float("-inf")

    current_value = node.value

    if current_value > maximum_value:
        maximum_value = current_value

    left_max = find_maximum_value(node.left, maximum_value=maximum_value)
    right_max = find_maximum_value(node.right, maximum_value=maximum_value)

    return max(left_max, right_max, maximum_value)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    print(solution(node4))
    assert solution(node4) == 3


if __name__ == "__main__":
    test()
