from collections import defaultdict
from pprint import pprint
import math


def read_input():
    n, m = map(int, input().split())
    adjacency_mapping = defaultdict(list)

    for _ in range(m):
        u, v, w = map(int, input().split())
        adjacency_mapping[u].append((v, w))
        adjacency_mapping[v].append((u, w))

    return adjacency_mapping, n, m


def find_min_dist_vertex(distances, visited):
    minimum = float("+inf")
    min_dist_vertex = None

    for i, dist in enumerate(distances):
        v = i + 1
        if dist < minimum and not visited[v - 1]:
            minimum = dist
            min_dist_vertex = v

    return min_dist_vertex


def relax(u, v, w, distances, previous):
    if distances[u - 1] + w < distances[v - 1]:
        distances[v - 1] = distances[u - 1] + w
        previous[v - 1] = u


def dijkstra(s, n, m, adjacency_mapping):
    visited = [False for _ in range(n)]
    distances = [float("+inf") for _ in range(n)]
    previous = [None for _ in range(n)]

    distances[s - 1] = 0

    while True:
        current = find_min_dist_vertex(distances, visited)

        if current is None:
            break

        for neighbor, w in adjacency_mapping[current]:
            relax(current, neighbor, w, distances, previous)

        visited[current - 1] = True

    return distances


def solve():
    adjacency_mapping, n, m = read_input()
    output_matrix = []

    for v in range(1, n + 1):
        distance_row = dijkstra(v, n, m, adjacency_mapping)
        output_matrix.append(distance_row)

    for row in output_matrix:
        print(*map(lambda x: -1 if math.isinf(x) else x, row))


if __name__ == "__main__":
    solve()
