import bisect


def lengthOfLIS(nums: list[int]) -> int:
    temp = []

    for num in nums:
        idx = bisect.bisect_left(temp, num)

        if idx < len(temp):
            temp[idx] = num
        else:
            temp.append(num)

    return len(temp)


print("Example 1: ", lengthOfLIS([10, 9, 2, 5, 3, 7, 108, 18]))
