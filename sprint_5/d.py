import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root1, root2) -> bool:
    return are_identical(root1, root2)


def are_identical(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None and node2 is not None:
        return False
    if node1 is not None and node2 is None:
        return False

    # NOTE: At this point, both nodes are not None.
    if node1.value != node2.value:
        return False

    return are_identical(
        node1.left,
        node2.left,
    ) and are_identical(
        node1.right,
        node2.right,
    )


def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == "__main__":
    test()
