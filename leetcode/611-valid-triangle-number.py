from typing import List
from bisect import bisect_left
def triangleNumber(nums: List[int]) -> int:
    nums.sort()

    cnt = 0
    for a in range(len(nums) - 2):
        for b in range(a + 1, len(nums) - 1):
            sumTwoSide = nums[a] + nums[b]
            insertion_point = bisect_left(nums, sumTwoSide, lo = b + 1)
            largest_valid_idx = insertion_point - 1
            cnt += largest_valid_idx - b

    return cnt

print("Example 1: ", triangleNumber([2,2,3,4]))
print("Example 2: ", triangleNumber([4,2,3,4]))