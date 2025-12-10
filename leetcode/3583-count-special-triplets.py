# 3583. Count Special Triplets
# Medium

"""
question:
    find special triplet

    0 <= i < j < k < n
    range goes [0, n)

    nums[i] == nums[j] ** 2
    nums[k] == nums[j] ** 2

intuition:

    can do two pointer approach on a sorted list
    cannot sort, order matters here

"""

from collections import defaultdict


def specialTriplets(nums: list[int]) -> int:
    mod = 10**9 + 7
    start = {}
    mid = {}
    res = 0

    for n in nums:
        res += mid.get(n / 2, 0)
        mid[n] = start.get(n * 2, 0) + mid.get(n, 0)
        start[n] = start.get(n, 0) + 1
    return res % mod


nums = [8, 4, 2, 8, 4]
print(f"Example 1: {nums}, Ans: {specialTriplets(nums)}")
