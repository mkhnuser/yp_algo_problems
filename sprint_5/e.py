import os

LOCAL = os.environ.get("REMOTE_JUDGE", "false") != "true"

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    return recurse_solution(root, float("-inf"), float("+inf"))


def recurse_solution(node, lower_bound, upper_bound) -> bool:
    if node is None:
        return True

    if node.value <= lower_bound or node.value >= upper_bound:
        return False

    return recurse_solution(
        node.left,
        lower_bound=lower_bound,
        upper_bound=node.value,
    ) and recurse_solution(
        node.right,
        lower_bound=node.value,
        upper_bound=upper_bound,
    )


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == "__main__":
    test()
