#medium
from typing import List
def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for num in numSet:
        if (num - 1) not in numSet:
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(longest, length)

    return longest

print("Example 1:", longestConsecutive([100,4,200,1,3,2]))
print("Example 2:", longestConsecutive([10,11,12,1,2,3]))
