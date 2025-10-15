def maxIncreasingSubarrays(nums: list[int]) -> int:
    precnt, cnt, ans = 0, 1, 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cnt += 1
        else:
            precnt, cnt = cnt, 1

        ans = max(ans, min(precnt, cnt))
        ans = max(ans, cnt // 2)

    return ans



print("Example 1:", maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))
print("Example 2:", maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]))
