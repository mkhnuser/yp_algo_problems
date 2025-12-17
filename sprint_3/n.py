def solve():
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    matrix.sort()

    if not matrix:
        return []

    # NOTE: Consider this: [[2, 3], [6, 10], [7, 8], [7, 8]].

    output = [matrix[0]]

    for start, end in matrix[1:]:
        latest_output = output[-1]
        latest_start, latest_end = latest_output

        if start <= latest_end:
            # NOTE: An overlap has been found, so carefully merge.
            latest_output[0] = min(start, latest_start)
            latest_output[1] = max(end, latest_end)
        else:
            # NOTE: start > latest_end, so no overlapping here, just append an interval.
            output.append([start, end])

    return output


if __name__ == "__main__":
    for interval in solve():
        print(" ".join(map(str, interval)))
