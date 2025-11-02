def majorityElement(nums: list[int]) -> int:
    res = m = 0

    for n in nums:
        if m == 0:
            res = n
        m += 1 if res == n else -1
    return res


print("Example 1: ", majorityElement([1, 1, 1, 4, 1]))
