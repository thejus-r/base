from typing import List
def sort(nums: List[int]) -> List[int]:
    quickSort(nums, 0, len(nums)-1)
    return nums


def quickSort(nums, lo, hi):
   if lo < hi:
      pi = partition(nums, lo, hi)

      quickSort(nums, lo, pi-1)
      quickSort(nums, pi+ 1, hi)

def partition(nums, lo, hi):
    pivot = nums[hi]

    i = lo - 1
    for j in range(lo, hi):
        if nums[j] < pivot:
            i += 1
            swap(nums, i, j)
    swap(nums, i + 1, hi)
    return i + 1

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

print("Example 1:", sort([9,8,7,6,5,4,3,2,1]))
