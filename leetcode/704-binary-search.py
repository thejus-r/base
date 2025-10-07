from typing import List
def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1

print(f"Example 1: ", search([-1,0,3,5,9,12], 9))
print(f"Example 2: ", search([-1,0,3,5,9,12], 2))