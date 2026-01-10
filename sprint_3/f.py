def main():
    n = int(input())
    nums = list(map(int, input().split()))

    maximum_perimeter = float("-inf")
    nums.sort()

    for i in range(len(nums) - 1, 1, -1):
        c = nums[i]
        b = nums[i - 1]
        a = nums[i - 2]

        if a + b > c:
            maximum_perimeter = max(maximum_perimeter, a + b + c)

    return maximum_perimeter


if __name__ == "__main__":
    print(main())
