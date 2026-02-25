from collections import defaultdict
from pprint import pprint


def find_not_visited_vertex_with_the_min_distance(visited, distance, adjacency_list):
    min_value = float("inf")
    min_vertex = None

    for v in adjacency_list:
        if not visited[v - 1] and distance[v - 1] < min_value:
            min_value = distance[v - 1]
            min_vertex = v

    return min_vertex


def do_dijkstra(s, n, visited, previous, distance, adjacency_list):
    for v in range(1, n + 1):
        distance[v - 1] = float("inf")
        previous[v - 1] = None
        visited[v - 1] = False

    distance[s - 1] = 0

    while True:
        u = find_not_visited_vertex_with_the_min_distance(
            visited,
            distance,
            adjacency_list,
        )
        if u is None or distance[u - 1] == float("inf"):
            break

        visited[u - 1] = True

        for tuple_ in adjacency_list[u]:
            v, weight = tuple_
            current_distance_to_v = distance[u - 1] + weight

            if distance[v - 1] > current_distance_to_v:
                distance[v - 1] = current_distance_to_v
                previous[v - 1] = u


def solve():
    n, m = map(int, input().split())
    adjacency_list = defaultdict(list)

    for _ in range(m):
        u, v, weight = map(int, input().split())
        adjacency_list[u].append((v, weight))
        adjacency_list[v].append((u, weight))

    # NOTE: OK, for each vertex u, find the shortest path to each other vertex v of the graph.
    # Then the resulting matrix[u-1][v-1] will contain the shortest path from u to v.
    # Since a graph is directed, this matrix is not necessarily symmetric.

    matrix = [[-1 for _ in range(n)] for __ in range(n)]

    visited = [False for _ in range(n)]
    previous = [None for _ in range(n)]
    distance = [None for _ in range(n)]

    for u in range(1, n + 1):
        do_dijkstra(u, n, visited, previous, distance, adjacency_list)
        matrix[u - 1] = [item if item != float("inf") else -1 for item in distance]

    for row in matrix:
        print(*row)


if __name__ == "__main__":
    solve()
