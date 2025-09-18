from typing import List
def binarySearch(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


list1 = [2, 3, 4, 10, 40]
print(binarySearch(list1, 10))

list2= [2, 3, 4, 10, 40, 50]
print(binarySearch(list2, 50))