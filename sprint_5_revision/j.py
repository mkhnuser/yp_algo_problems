import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if not LOCAL:
    from node import Node

if LOCAL:

    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert(root, key) -> Node:
    new_node = Node(value=key)
    recurse_insert_node(root, new_node)
    return root


def recurse_insert_node(current_node, new_node):
    if current_node.value <= new_node.value:
        if not current_node.right:
            current_node.right = new_node
        else:
            recurse_insert_node(current_node.right, new_node)
    else:
        if not current_node.left:
            current_node.left = new_node
        else:
            recurse_insert_node(current_node.left, new_node)


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == "__main__":
    test()
