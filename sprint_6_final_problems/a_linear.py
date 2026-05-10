from pprint import pprint


def find_max_edge_spanning_from_max_spanning_tree(
    visited_verticies,
    adj_mapping,
):
    from_vertex = None
    max_vertex = None
    max_edge_weight = float("-inf")

    for u, incident_edges in adj_mapping.items():
        if u not in visited_verticies:
            # NOTE: We've encounted a node which is not in our maximum spanning tree.
            continue

        for edge in incident_edges:
            v, w = edge

            if w > max_edge_weight and v not in visited_verticies:
                from_vertex = u
                max_vertex = v
                max_edge_weight = w

    return from_vertex, max_vertex, max_edge_weight


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

    mst_edges = set()
    visited_verticies = set()
    visited_verticies.add(starting_vertex)

    while True:
        from_vertex, max_vertex, max_edge_weight = (
            find_max_edge_spanning_from_max_spanning_tree(
                visited_verticies,
                adj_mapping,
            )
        )

        if not from_vertex:
            # NOTE: A maximum spanning tree has been constructed.
            break

        visited_verticies.add(max_vertex)
        mst_edges.add((from_vertex, max_vertex, max_edge_weight))

    return sum((weight for (u, v, weight) in mst_edges))


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
