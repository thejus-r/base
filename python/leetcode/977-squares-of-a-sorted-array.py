# 977. Squares of a Sorted Array
# Easy


def sortedSquares(nums: list[int]) -> list[int]:
    res = []
    left, right = 0, len(nums) - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res.append(nums[left] ** 2)
            left += 1
        else:
            res.append(nums[right] ** 2)
            right -= 1

    return res[::-1]


nums = [-4, -1, 0, 3, 10]
print(f"Example 1: {sortedSquares(nums)}")
