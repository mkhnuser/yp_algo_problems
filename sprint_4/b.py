def solve():
    n = int(input())
    rounds = input().replace(" ", "")

    summation = 0
    first_seen = {0: -1}
    max_len = 0

    for i, char in enumerate(rounds):
        if char == "1":
            summation += 1
        else:
            summation -= 1

        if summation in first_seen:
            max_len = max(max_len, i - first_seen[summation])
        else:
            first_seen[summation] = i

    print(max_len)


if __name__ == "__main__":
    solve()
