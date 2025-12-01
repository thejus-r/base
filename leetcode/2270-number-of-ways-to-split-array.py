# 2270. Number of Ways to Split Array
# Medium

"""
Intitution:
    we find the prefix sum, so it easier to calculate sum of nums[i, j] just by taking the difference

    if nums[i] >= nums[-1] - nums[i]


"""


def waysToSplitArray(nums: list[int]) -> int:
    res = 0
    totalSum = sum(nums)
    prefix = 0

    for i in range(0, len(nums) - 1):
        prefix += nums[i]
        if prefix >= totalSum - prefix:
            res += 1

    return res


print("Example 1: ", waysToSplitArray([10, 4, -8, 7]))
print("Example 2: ", waysToSplitArray([2, 3, 1, 0]))
