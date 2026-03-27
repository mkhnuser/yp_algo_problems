def solve_incrementally():
    M = int(input())
    n = int(input())
    golden_heaps = []

    for _ in range(n):
        c, m = map(int, input().split())
        golden_heaps.append([c, m])

    # NOTE: Greedily take the most precious sand.
    golden_heaps.sort(key=lambda heap: heap[0], reverse=True)

    weight = 0
    cost = 0

    for heap in golden_heaps:
        # NOTE: Total cost of a heap is c * m.
        c, m = heap

        if M >= weight + m:
            weight += m
            cost += c * m
        else:
            # NOTE: M < weight + m, so greedily stuff your pockets.
            while weight < M:
                weight += 1
                cost += c

    return cost


def solve_eff():
    M = int(input())
    n = int(input())
    golden_heaps = []

    for _ in range(n):
        c, m = map(int, input().split())
        golden_heaps.append([c, m])

    # NOTE: Greedily take the most precious sand.
    golden_heaps.sort(key=lambda heap: heap[0], reverse=True)

    weight = 0
    cost = 0

    for c, m in golden_heaps:
        if weight == M:
            break

        w = min(m, M - weight)

        weight += w
        cost += w * c

    return cost


if __name__ == "__main__":
    print(solve_eff())
