def main():
    n, k = map(int, input().split())
    costs = list(map(int, input().split()))

    costs.sort()
    counter = 0

    for cost in costs:
        diff = k - cost

        if diff >= 0:
            counter += 1
            k -= cost
        else:
            break

    return counter


if __name__ == "__main__":
    print(main())
