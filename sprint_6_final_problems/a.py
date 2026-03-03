# https://contest.yandex.ru/contest/25070/run-report/157916016/
#
# --- ПРИНЦИП РАБОТЫ
# Алгоритм является почти точной копией алгоритма Прима для поиска минимального остовного дерева.
# Вместо поиска веса минимального остовного дерева, мы ищим вес максимального остовного дерева,
# жадно находя ветвь с максимальным весом, которая исходит из остовного дерева.
#
# Для поиска максимального веса используется очередь с приоритетом на базе библиотеки heapq.
# По умолчанию heapq - минимальная очередь, поэтому мы используем унарный минус, чтобы получить максимальную очередь.
#
# Отдельное внимание уделяем валидации входного графа.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# Такая же, как и у алгоритма Прима, т.е. O(m * log(n)), где m - кол-во рёбер, а n - кол-во вершин.
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(n * m) - в худшем случае приоритетная очередь содержит весь граф.


import heapq
from collections import defaultdict


INVALID_GRAPH_MESSAGE = "Oops! I did it again"


def check_if_graph_is_valid(mapping, n, m):
    if not mapping.keys():
        raise Exception("Invalid graph!")

    for i in range(1, n + 1):
        if i not in mapping.keys():
            raise Exception("Invalid graph!")


def solve():
    n, m = map(int, input().split())
    mapping = defaultdict(list)

    for _ in range(m):
        u, v, w = map(int, input().split())
        mapping[u].append((v, w))
        mapping[v].append((u, w))

    if n == 1 and m == 0:
        # NOTE: Handle a special case for a graph with only one vertex.
        print(0)
        return

    try:
        check_if_graph_is_valid(mapping, n, m)
    except Exception:
        print(INVALID_GRAPH_MESSAGE)
        return

    print(calculate_max_weight(1, mapping, n))


def calculate_max_weight(starting_vertex, mapping, n):
    visited = [False] * n
    priority_queue = []
    total_weight = 0
    default_weight = 0

    heapq.heappush(priority_queue, (-default_weight, starting_vertex))

    while priority_queue:
        weight, u = heapq.heappop(priority_queue)

        if visited[u - 1]:
            continue

        total_weight += abs(weight)
        visited[u - 1] = True

        for v in mapping[u]:
            if not visited[v[0] - 1]:
                heapq.heappush(priority_queue, (-v[1], v[0]))

    return total_weight


if __name__ == "__main__":
    solve()
