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
from pprint import pprint


def find_maximum_spanning_tree_weight(n, m, adj_mapping):
    if not adj_mapping:
        # NOTE: No connections whatsoever.
        return 0

    # NOTE: A graph can be disconnected.
    # What do you do in this case?

    starting_vertex = None
    for u, incident_edges in adj_mapping.items():
        starting_vertex = u

    if starting_vertex is None:
        raise RuntimeError("There is no starting vertex!")

    visited_verticies = set()
    min_heap = []
    total_weight = 0
    heapq.heappush(min_heap, (-0, starting_vertex))

    while min_heap:
        w, v = heapq.heappop(min_heap)

        if v in visited_verticies:
            continue

        w = -w
        total_weight += w

        for n, weight in adj_mapping[v]:
            heapq.heappush(min_heap, (-weight, n))

        visited_verticies.add(v)

    return total_weight


def solve():
    n, m = map(int, input().split())
    adj_mapping = {}

    for _ in range(m):
        u, v, w = map(int, input().split())

        if u not in adj_mapping:
            adj_mapping[u] = []
        adj_mapping[u].append((v, w))

        if v not in adj_mapping:
            adj_mapping[v] = []
        adj_mapping[v].append((u, w))

    if n == 1 and m == 0:
        # NOTE: Handle a special case for a graph with only one vertex.
        return 0

    for i in range(1, n + 1):
        if i not in adj_mapping.keys():
            return "Oops! I did it again"

    weight = find_maximum_spanning_tree_weight(n, m, adj_mapping)

    if weight == 0:
        return "Oops! I did it again"

    return weight


if __name__ == "__main__":
    # NOTE: The solution is fine, although it time limits since heap should be used.
    print(solve())
