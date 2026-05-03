import os
from queue import Queue

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def print_range(node, l, r):
    output = []

    def inorder(n):
        if n is None:
            return

        if n.value >= l:
            inorder(n.left)

        if l <= n.value <= r:
            output.append(n.value)

        if n.value <= r:
            inorder(n.right)

    inorder(node)
    print(*output)


def find_successor(root, node):
    if node.right is not None:
        return find_min(node.right)
    return recurse_find_successor(root, node, None)


def recurse_find_successor(y, x, c):
    if y == x:
        return c
    if x.value <= y.value:
        return recurse_find_successor(y.left, x, y)
    else:
        return recurse_find_successor(y.right, x, c)


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def find_smallest(node, l, r, smallest):
    if node is None:
        return smallest
    if node.value < l:
        return find_smallest(node.right, l, r, smallest)
    if node.value >= l:
        smallest = node
        return find_smallest(node.left, l, r, smallest)


def bfs(node, l, r):
    q = Queue()
    q.put(node)
    output = []

    while q.qsize() > 0:
        c = q.get()
        if c.value >= l and c.value <= r:
            output.append(c.value)
        if c.left is not None:
            q.put(c.left)
        if c.right is not None:
            q.put(c.right)

    output.sort()
    print(*output)


def lmr_fully(node, output, l, r):
    if node is None:
        return

    lmr_fully(node.left, output, l, r)
    if node.value >= l and node.value <= r:
        output.append(node.value)
    lmr_fully(node.right, output, l, r)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


if __name__ == "__main__":
    test()
