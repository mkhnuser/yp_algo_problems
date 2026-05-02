def solve():
    intervals = []

    n = int(input())
    for _ in range(n):
        string = input()
        interval = list(map(int, string.split()))
        intervals.append(interval)

    intervals.sort()

    output = []
    output.append(intervals[0])

    for interval_index in range(1, len(intervals)):
        current_interval = intervals[interval_index]
        previous_interval = output.pop()

        current_start, current_end = current_interval
        previous_start, previous_end = previous_interval

        if current_start <= previous_end:
            new_start = previous_start
            new_end = max(previous_end, current_end)
            new_interval = [new_start, new_end]
            output.append(new_interval)
        else:
            output.append(previous_interval)
            output.append(current_interval)

    return output


if __name__ == "__main__":
    for output in solve():
        print(*output)
