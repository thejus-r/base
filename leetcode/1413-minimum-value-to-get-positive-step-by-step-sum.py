# 1413. Minimum Value to Get Positive Step by Step Sum
# Easy

def minStartValue(nums: list[int]) -> int:
    n = len(nums)
    for i in range(1, n):
        nums[i] += nums[i - 1]

    minVal = min(nums)
    return abs(minVal) + 1 if minVal < 0 else 1

print("Example 1: ", minStartValue([-3,2,-3,4,2]))
print("Example 2: ", minStartValue([1, 2]))
print("Example 3: ", minStartValue([1, -2, -3]))
print("Example 4: ", minStartValue([2,3,5,-5,-1]))
