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


def remove(root, key) -> Optional[Node]:
    if not root:
        return root

    find_res = find_node_and_its_parent(None, root, key)

    if not find_res:
        # NOTE: The node has not been found, do not change anything.
        return root

    # NOTE: d is the node to be deleted, p_d is the parent of d.
    # n is the node which takes place of d, p_n is the parent of n.

    p_d, d = find_res
    if not d.left and not d.right:
        # NOTE: d has no children, so just erase it from the tree.

        if not p_d:
            # NOTE: d has no children and d has no parent, so d is the root.
            # So, the new root becomes None.
            return None

        if p_d.left is d:
            p_d.left = None
        else:
            p_d.right = None

        return root

    if d.left and not d.right:
        # NOTE: d has only left child.
        if not p_d:
            # NOTE: d has only one child and d has no parent, so d is the root.
            return d.left

        if p_d.left is d:
            p_d.left = d.left
        else:
            p_d.right = d.left

        return root

    if not d.left and d.right:
        if not p_d:
            return d.right

        if p_d.left is d:
            p_d.left = d.right
        else:
            p_d.right = d.right

        return root

    else:
        # NOTE: d has both children.

        p_n, n = find_max(d, d.left)

        if n.left is None:
            # NOTE: n has no left child.
            p_n.right = None

            if p_d:
                if p_d.left is d:
                    p_d.left = n
                else:
                    p_d.right = n
            else:
                root = n

            n.left = d.left
            n.right = d.right
        else:
            # NOTE: n has a left child.
            p_n.right = n.left

            if p_d:
                if p_d.left is d:
                    p_d.left = n
                else:
                    p_d.right = n
            else:
                root = n

            n.left = d.left
            n.right = d.right

        return root


def find_node_and_its_parent(
    parent_of_current,
    current,
    value,
) -> Optional[tuple[Optional[Node], Node]]:
    if current is None:
        return None
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
