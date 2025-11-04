def longestOnes(nums: list[int], k: int) -> int:
    max_length, zero_count, left = 0, 0, 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length


print("Example 1: ", longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
