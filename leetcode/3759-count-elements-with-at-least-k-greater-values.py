def countElements(nums: list[int], k: int) -> int:
    if k == 0:
        return len(nums)

    nums.sort()
    n = len(nums)

    th = nums[n - k]
    ans = 0
    print(nums)
    print("Th", th)
    for n in nums:
        if n < th:
            ans += 1

    return ans


print("Example 1: ", countElements([3, 1, 2], 1))
print("Example 2: ", countElements([5, 5, 5], 2))
