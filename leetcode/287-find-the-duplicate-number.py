# cyclic sort

from typing import List
def findDuplicate(nums: List[int]) -> int:
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if i < len(nums) and nums[i] != nums[correct]:
            temp = nums[i]
            nums[i] = nums[correct]
            nums[correct] = temp
        else:
            i += 1

    for i in range(len(nums)):
        if i != nums[i] - 1:
            return nums[i]

    return len(nums)

print(f"Example 1: ", findDuplicate([1, 3, 4, 2, 2]))
print(f"Example 2: ", findDuplicate([3, 1, 3, 4, 2]))
print(f"Example 3: ", findDuplicate([3, 3, 3, 3, 3]))