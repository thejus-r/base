from typing import List
class NumArray:
    def __init__(self, nums: List[int]) -> None:
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] =  self.nums[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]

        return self.nums[right] - self.nums[left - 1]

numArr = NumArray([1,2,3,4,5])
print(numArr.nums)
print(numArr.sumRange(0,3))
print(numArr.sumRange(1,3))
