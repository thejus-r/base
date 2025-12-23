def binarySearch(nums: list[int], target: int) -> int:
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


# binary search with right bias
def binarySearchWithRightBias(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return lo


list3 = [10, 40, 50, 50, 50, 50, 100]
idx = binarySearchWithRightBias(list3, 50)
print(list3[idx] == 50)
list3.insert(idx, 50)
print("idx: ", idx, " len:", len(list3))
print("list: ", list3)
