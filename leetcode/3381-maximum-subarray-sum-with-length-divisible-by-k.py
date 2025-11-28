# 3381. Maximum Subarray Sum With Length Divisible by K
# Medium

"""
Intuition:
    - We find the prefix sum

"""

import sys


def maxSubArraySum2(nums: list[int], k: int) -> int:
    # used to store, the min reminder
    prefix = [sys.maxsize] * k
    prefix[0] = 0
    res = -sys.maxsize
    total = 0

    for i, n in enumerate(nums):
        total += n
        length = i + 1
        prefix_len = length % k
        res = max(res, total - prefix[prefix_len])
        prefix[prefix_len] = min(prefix[prefix_len], total)

    return res


# print("Example 1: ", maxSubArraySum2([1, 2], 1))
# print("Example 2: ", maxSubArraySum2([-1, -2, -3, -4, -5], 4))
print("Example 3: ", maxSubArraySum2([-5, 1, 2, -3, 4], 2))


# This one TLE on leetcode
"""
Intuition:
    since we are finding the max sum of subarray of length divisible by k
    the sizes of the subarray lengths has to be mulitiples of k

    for example when k is 2, the size can be 2, 4, 6, 8 etc and has to be
    lesser than the len(nums)

    can i use sliding window with variying window size,
    should i try all window sizes since nums can be -ve or +ve nums


"""


def maxSubarraySum(nums: list[int], k: int) -> int:
    n = len(nums)
    maxSum = -float("inf")
    currWindow = k

    while currWindow <= n:
        currSum = sum(nums[:currWindow])
        maxSum = max(currSum, maxSum)
        for i in range(currWindow, n):
            currSum -= nums[i - currWindow]
            currSum += nums[i]

            maxSum = max(currSum, maxSum)

        currWindow += k

    return int(maxSum)


# print("Example 1: ", maxSubArraySum2([1, 2], 1))
# print("Example 2: ", maxSubArraySum2([-1, -2, -3, -4, -5], 4))
# print("Example 3: ", maxSubArraySum2([-5, 1, 2, -3, 4], 2))
