import os
from queue import Queue

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    # return pre_order(root, maximum=float("-inf"))
    # return bfs(root)
    return find_max(root, float("-inf"))


def pre_order(node, maximum):
    if node is None:
        return maximum

    if node.value > maximum:
        maximum = node.value

    left_maximum = pre_order(node.left, maximum)
    right_maximum = pre_order(node.right, maximum)
    return left_maximum if left_maximum > right_maximum else right_maximum


def bfs(node):
    q = Queue()
    q.put(node)
    maximum = float("-inf")

    while q.qsize() > 0:
        c = q.get()

        if c.value > maximum:
            maximum = c.value

        if c.left is not None:
            q.put(c.left)
        if c.right is not None:
            q.put(c.right)

    return maximum


def find_max(node, max_so_far):
    if node is None:
        return max_so_far

    if node.value > max_so_far:
        max_so_far = node.value

    left_max = find_max(node.left, max_so_far)
    right_max = find_max(node.right, max_so_far)
    return max(left_max, max_so_far, right_max)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == "__main__":
    test()
