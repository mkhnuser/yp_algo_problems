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
    node_to_delete = find_node(root, key)

    if node_to_delete is None:
        return root

    return _remove(root, node_to_delete)


def _remove(current, node_to_delete):
    if current.value > node_to_delete.value:
        if current.left is not None:
            current.left = _remove(current.left, node_to_delete)
        return current
    elif current.value < node_to_delete.value:
        if current.right is not None:
            current.right = _remove(current.right, node_to_delete)
        return current

    # NOTE: current.value == node_to_delete.value at this point.
    if node_to_delete.left is None:
        return node_to_delete.right
    elif node_to_delete.right is None:
        return node_to_delete.left

    # NOTE: OK, node_to_delete now has two children.
    successor = get_min(node_to_delete.right)
    _remove(current, successor)
    successor.left = node_to_delete.left
    successor.right = node_to_delete.right

    return successor


def get_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def find_node(current_node, key):
    if current_node is None:
        return None
    if current_node.value == key:
        return current_node

    if current_node.value > key:
        return find_node(current_node.left, key)
    return find_node(current_node.right, key)


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


if __name__ == "__main__":
    test()
