# 1262. Greatest Sum Divisible by Three
# Medium


def maxSumDivThree(nums: list[int]) -> int:
    minMod1 = float("inf")
    minMod2 = float("inf")

    sum = 0
    for n in nums:
        sum += n
        if n % 3 == 1:
            minMod2 = min(minMod2, n + minMod1)
            minMod1 = min(minMod1, n)
        if n % 3 == 2:
            minMod1 = min(minMod1, n + minMod2)
            minMod2 = min(minMod2, n)

    if sum % 3 == 0:
        return sum
    elif sum % 3 == 1:
        return sum - int(minMod1)
    else:
        return sum - int(minMod2)


print("Example 1:", maxSumDivThree([3, 6, 5, 1, 8]))
print("Example 2:", maxSumDivThree([4]))
print("Example 3:", maxSumDivThree([1, 2, 3, 4, 4]))
print("Example 4:", maxSumDivThree([2, 6, 2, 2, 7]))
