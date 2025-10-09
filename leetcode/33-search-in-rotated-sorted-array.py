def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < nums[hi]:
            hi = mid
        else:
            lo = mid + 1

    pivot = lo  # pivot to do another binary search

    l, r = 0, len(nums) - 1

    if target >= nums[pivot] and target <= nums[r]:
        l = pivot
    else:
        r = pivot - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1


print(f"Example 1: {search([4, 5, 6, 7, 0, 1, 2], 0)}")  # 4
print(f"Example 2: {search([4, 5, 6, 7, 0, 1, 2], 3)}")  # -1
print(f"Example 3: {search([1], 0)}")  # -1
