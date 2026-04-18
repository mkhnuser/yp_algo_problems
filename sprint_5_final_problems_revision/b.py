# https://contest.yandex.ru/contest/24810/run-report/157251922/

from typing import Optional
import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def handle_no_children_removal(p_d, d, root):
    if p_d is None:
        # NOTE: d has no children and d has no parent, so d is the root.
        # So, the new root becomes None.
        return None

    if p_d.left is d:
        p_d.left = None
    else:
        p_d.right = None

    return root


def handle_one_child_removal(p_d, d, root):
    # NOTE: d has only one child.
    if p_d is None:
        return d.left if d.left is not None else d.right

    if p_d.left is d:
        p_d.left = d.left if d.left is not None else d.right
    else:
        p_d.right = d.left if d.left is not None else d.right

    return root


def remove(root, key) -> Optional[Node]:
    # NOTE: The function has to return the root.
    if root is None:
        return root

    p_d, d = find_node_and_its_parent(None, root, key)

    if d is None:
        # NOTE: The node has not been found, do not change anything.
        return root

    if d.left is None and d.right is None:
        return handle_no_children_removal(p_d, d, root)

    if d.left is None or d.right is None:
        return handle_one_child_removal(p_d, d, root)
    else:
        # NOTE: d has both children.

        # NOTE: Find the parent of the predecessor and the predecessor itself.
        p_n, n = find_max(d, d.left)

        # NOTE: If d is the parent of the predecessor,
        # then just drag the predecessor on the place of d.
        # ---
        # Otherwise, handle the possible child of the predecessor.
        if d is not p_n:
            remove(p_n, n.value)
            n.left = d.left

        if p_d is not None:
            if p_d.left is d:
                p_d.left = n
            else:
                p_d.right = n
        else:
            root = n

        n.right = d.right
        return root


def find_node_and_its_parent(
    parent_of_current,
    current,
    value,
) -> tuple[Node | None, Node | None]:
    if current is None:
        return None, None
    if current.value == value:
        return parent_of_current, current
    elif current.value < value:
        return find_node_and_its_parent(current, current.right, value)
    else:
        return find_node_and_its_parent(current, current.left, value)


def find_max(parent_of_current, current) -> tuple[Node, Node]:
    while current.right:
        parent_of_current = current
        current = current.right
    return parent_of_current, current


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8


def test_find():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    assert find_node_and_its_parent(None, node7, 2) == (node2, node1)
    assert find_node_and_its_parent(None, node7, 5) == (None, node7)
    assert find_node_and_its_parent(None, node7, 8) == (node6, node5)


def test_find_max():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    assert find_max(node7, node3) == (node3, node2)
    assert find_max(None, node7) == (node7, node6)


if __name__ == "__main__":
    test()
    test_find()
    test_find_max()
