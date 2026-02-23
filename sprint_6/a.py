# https://contest.yandex.ru/contest/25069/problems/?nc=WJLDhseT
from collections import defaultdict


def solve():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        v, u = map(int, input().split())
        mapping[v].append(u)

    # NOTE: Example of what we've obtained at this point: defaultdict(<class 'list'>, {1: [3], 2: [3], 5: [2]}).

    for list_ in mapping.values():
        list_.sort()

    for i in range(1, n + 1):
        # NOTE: i = 1 .. 100.
        node_in_question = i
        adjacency_list = mapping[node_in_question]

        if adjacency_list:
            print(f"{len(adjacency_list)} {' '.join(map(str, adjacency_list))}")
        else:
            print(0)


if __name__ == "__main__":
    solve()
