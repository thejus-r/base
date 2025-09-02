# easy

from typing import List
def twoSum(nums: List[int], target:int) -> List[int]:
    dict = {}
    res = []
    for i in range(len(nums)):
        if dict.get(nums[i]) != None:
            res.append(dict.get(nums[i]))
            res.append(i)
            break
        reminder =  target - nums[i]
        dict.update({ reminder: i })

    return res

print("Example 1:", twoSum([2,7,11, 15], 9))
print("Example 2:", twoSum([3,2,4], 6))
