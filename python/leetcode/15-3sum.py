# 15. 3Sum
# Medium


def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        j, k = i + 1, len(nums) - 1
        while j < k:
            s = a + nums[j] + nums[k]
            if s < 0:
                j += 1
            elif s > 0:
                k -= 1
            else:
                res.append([a, nums[j], nums[k]])
                j += 1
                while nums[j] == nums[j - 1] and j < k:
                    j += 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
print(f"Example 1: {threeSum(nums)}")

nums = [0, 0, 0, 0]
print(f"Example 2: {threeSum(nums)}")
