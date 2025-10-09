def findMin(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        m = lo + (hi - lo) // 2
        if nums[m] < nums[hi]:
            hi = m
        else:
            lo = m + 1
    return nums[lo]


print(f"Example 1: {findMin([3, 4, 5, 1, 2])}")
print(f"Example 1: {findMin([4, 5, 6, 7, 0, 1, 2])}")
