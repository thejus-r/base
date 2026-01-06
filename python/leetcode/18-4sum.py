# 18. 4Sum
# Medium


def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()

    def kSum(nums, target, k):
        res = []
        if not nums:
            return res

        avg_val = target // k

        if avg_val < nums[0] or nums[-1] < avg_val:
            return res

        if k == 2:
            return twoSum(nums, target)

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in kSum(nums[i + 1 :], target - nums[i], k - 1):
                    res.append([nums[i]] + subset)

        return res

    def twoSum(nums, target: int):
        left, right = 0, len(nums) - 1
        res = []
        while left < right:
            two_sum = nums[left] + nums[right]

            if target > two_sum or (left > 0 and nums[left] == nums[left - 1]):
                left += 1
            elif target < two_sum or (
                right < right - 1 and nums[right] == nums[right + 1]
            ):
                right -= 1
            else:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1

        return res

    return kSum(nums, target, 4)


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(f"Example 1: {fourSum(nums, target)}")

nums = [2, 2, 2, 2, 2]
target = 8
print(f"Example 2: {fourSum(nums, target)}")
