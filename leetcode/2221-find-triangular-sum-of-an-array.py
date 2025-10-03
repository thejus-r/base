from typing import List
def triangularSum(nums: List[int]) -> int:
    N = len(nums)

    for i in range(N):
        for j in range(N - i - 1):
            nums[j] = (nums[j] + nums[j + 1]) % 10

    print(nums)
    return nums[0]

print("Example 1: ", triangularSum([1,2,3,4,5]))
print("Example 2: ", triangularSum([5]))
