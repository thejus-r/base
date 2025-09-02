from typing import List
def jump(nums: List[int]) -> int:
    n = len(nums)
    res = 0
    l = r = 0

    while(r < n - 1):
        farthest = 0
        for i in range(l ,r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        res += 1
    return res


print("Example 1:", jump([2, 3, 1, 1, 4])) # 2
print("Example 2:", jump([2, 3, 0, 1, 4])) # 2
