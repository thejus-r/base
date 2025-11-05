# 3318. Find X-Sum of All K-Long Subarrays I
# Easy

"""
inituition:
    since k is fixed, as we have xSum all Subarrays
    seems like a Sliding Window problem

    for each window iteration, we heapify the (key, value) tuple with a max heap
    the pop it x times to get the values that satisfies the condition

    when moving to next next window: update the value
    reduce the freq of the leaving value and increase the freq for the incoming value
"""

import collections
from heapq import heapify, heappop


def findXSum(nums: list[int], k: int, x: int) -> list[int]:
    # returns the xSum
    def xsum(ft: dict[int, int]):
        h = [(-freq, -value) for value, freq in ft.items()]
        heapify(h)
        s, y = 0, 0
        while y < x and len(h) > 0:
            freq, value = heappop(h)
            s += value * freq
            y += 1
        return s

    # initialize window, find freq of first k elements
    ans: list[int] = []
    freq_table: dict[int, int] = collections.defaultdict(int)
    for n in nums[:k]:
        freq_table[n] += 1

    ans.append(xsum(freq_table))

    for i in range(k, len(nums)):
        freq_table[nums[i]] += 1
        freq_table[nums[i - k]] -= 1
        ans.append(xsum(freq_table))

    return ans


# print("Example 1: ", findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2))
print("Example 2: ", findXSum([9, 2, 2], 3, 3))
