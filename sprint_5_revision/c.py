import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    left_lmr_order = []
    right_lmr_order = []
    construct_lmr(root.left, left_lmr_order)
    construct_lmr(root.right, right_lmr_order)
    left_lmr_order.reverse()
    return left_lmr_order == right_lmr_order


def construct_lmr(node, lmr_order):
    if node is None:
        return

    construct_lmr(node.left, lmr_order)
    lmr_order.append(node.value)
    construct_lmr(node.right, lmr_order)


def test():
    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)


if __name__ == "__main__":
    test()
