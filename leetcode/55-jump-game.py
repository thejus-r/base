from typing import List
def canJump(nums: List[int]) -> bool:
    N = len(nums)
    goal = N - 1

    for i in range(N - 1, -1, -1):
        max_jump = nums[i]
        if max_jump + i >= goal:
            goal = i

    if goal == 0:
        return True
    return False

print("Example 1: ", canJump([2,3,1,1,4]))
print("Example 2: ", canJump([3,2,1,0,4]))
