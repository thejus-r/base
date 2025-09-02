# Leetcode: 217
# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate
# easy

from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)

    return False

print("Example 1:", containsDuplicate([1,2,3,1]))
print("Example 2:", containsDuplicate([1,2,3,4]))
