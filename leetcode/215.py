# Leetcode: 215
# Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array
# medium

from heapq import heapify, heappop
from typing import List
def findKthLargest(nums: List[int], k: int) -> int:
    k = len(nums) - k

    heapify(nums)

    while (k > 0):
        heappop(nums)
        k -= 1


    return heappop(nums)


print("Example 1:", findKthLargest([3,2,1,5,6,4], 2)) # 5
print("Example 2:", findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
