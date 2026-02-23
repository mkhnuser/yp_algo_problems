def solve():
    n, m = map(int, input().split())
    adjacency_matrix = {v: [] for v in range(1, n + 1)}

    for _ in range(m):
        u, v = map(int, input().split())
        adjacency_matrix[u].append(v)
        adjacency_matrix[v].append(u)

    for node in adjacency_matrix:
        adjacency_matrix[node].sort()

    def dfs(adjacency_matrix, s):
        visited = set()
        stack = [s]
        output = []

        while stack:
            n = stack.pop()

            if n not in visited:
                visited.add(n)
                output.append(n)

                for neighbor in reversed(adjacency_matrix[n]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return output

    s = int(input())
    print(*dfs(adjacency_matrix, s))


if __name__ == "__main__":
    solve()
