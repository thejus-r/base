# medium
from typing import List
def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    def backtrack(i):
        if i >= len(nums):
            res.append(subset.copy())
        subset.append(nums[i])
        backtrack(i + 1)
        subset.pop()
        backtrack(i + 1)
    backtrack(0)
    return res

print("Example 1:", subsets([1,2,3]))
print("Example 2:", subsets([0]))
print("Example 2:", subsets([1,2,2]))
