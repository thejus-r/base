from typing import List
def largestPerimeter(nums: List[int]) -> int:
    nums.sort(reverse=True)

    def validTriangle(a, b, c):
        return a + b > c and b + c > a and a + c > b

    for n in range(len(nums) - 2):
        if validTriangle(nums[n], nums[n + 1], nums[n + 2]):
            return nums[n] +  nums[n + 1] + nums[n + 2]

    return 0

print("Example 1: ", largestPerimeter([2,1,2]))
print("Example 2: ", largestPerimeter([1,2,1,10]))