# https://contest.yandex.ru/contest/25070/run-report/158130962/
#
# --- ПРИНЦИП РАБОТЫ
# Задача похожа на задачу о поиске пути из лабиринта,
# за исключением того, что мы не можем использовать рекурсию из-за ограничения ввода,
# поэтому алгоритм построен на итеративном DFS:
# мы строим матрицу посещения, где отражаем, какие вершины уже были посещены,
# а вместо рекурсии используем стек.
#
# Если элемент не был посещён, лежит в рамках матрицы, и валиден,
# мы исследуем его и его потомки. При этом, если локальный размер острова больше максимального,
# мы обновляем наш максимум.
#
# --- ВРЕМЕННАЯ СЛОЖНОСТЬ
# O(n * m), где n * m - размер входной матрицы.
#
# --- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ
# O(n * m) - в худшем случае наш стек содержит каждый элемент входной матрицы.


def explore_dfs(i, j, rows, columns, visited, matrix):
    if i < 0 or i >= rows or j < 0 or j >= columns:
        return 0
    if visited[i][j]:
        return 0
    if matrix[i][j] != "#":
        return 0

    visited[i][j] = True
    current_size = 1

    # NOTE: Recursively go top, right, bottom, left.
    directions = [
        (i + 1, j),
        (i, j + 1),
        (i - 1, j),
        (i, j - 1),
    ]
    for next_i, next_j in directions:
        current_size += explore_dfs(next_i, next_j, rows, columns, visited, matrix)

    return current_size


def solve():
    n, m = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(n)]

    if not matrix:
        print("0 0")
        return

    rows = len(matrix)
    columns = len(matrix[0])
    visited = [[False] * columns for _ in range(rows)]

    island_count = 0
    max_size = 0

    for i in range(rows):
        for j in range(columns):
            current = matrix[i][j]
            if current == "#" and not visited[i][j]:
                island_count += 1
                stack = [(i, j)]
                visited[i][j] = True
                island_size = 0

                while stack:
                    current_i, current_j = stack.pop()
                    island_size += 1

                    # NOTE: Iteratively go top, right, bottom, left.
                    directions = [
                        (current_i + 1, current_j),
                        (current_i, current_j + 1),
                        (current_i - 1, current_j),
                        (current_i, current_j - 1),
                    ]
                    for next_i, next_j in directions:
                        if (
                            next_i < 0
                            or next_i >= rows
                            or next_j < 0
                            or next_j >= columns
                        ):
                            continue
                        if visited[next_i][next_j]:
                            continue
                        if matrix[next_i][next_j] != "#":
                            continue

                        stack.append((next_i, next_j))
                        visited[next_i][next_j] = True

                max_size = max(max_size, island_size)

    print(f"{island_count} {max_size}")


if __name__ == "__main__":
    solve()
