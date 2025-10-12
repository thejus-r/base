def runningSum(nums: list[int]) -> list[int]:
    for i in range(1,  len(nums) - 1):
        nums[i] += nums[i - 1]

    return nums

print("Example 1: ", runningSum([1,2,3,4]))
