# 1493. Longest Subarray of 1's After Deleting One Element
# Medium

"""
initution:
    solve with a window,
    can have atmost 1 zero, (which can be deleted)
    if another zero is found, shrink the left pointer

     max_length = right - left + 1

     case for: [1, 1, 1] -> max is 2
     if delete_count is zero, then we havent deleted anything, so reduce 1
"""


def longestSubarray(nums: list[int]) -> int:
    delete_count, left, max_length = 0, 0, 0

    for right in range(len(nums)):
        if nums[right] == 0:
            delete_count += 1
        while delete_count > 1:
            if nums[left] == 0:
                delete_count -= 1
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length - 1


print("Example 1: ", longestSubarray([1, 1, 0, 1]))
print("Example 2: ", longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print("Example 3: ", longestSubarray([1, 1, 1]))
