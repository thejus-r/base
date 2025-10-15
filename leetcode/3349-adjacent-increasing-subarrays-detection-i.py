def hasIncreasingSubarrays(nums: list[int], k: int) -> bool:
    n = len(nums)
    if n < k * 2:
        return False

    def increasing(arr: list[int]):
        return all([arr[x] > arr[x - 1] for x in range(1, len(arr))])

    for i in range(0,n - (2 * k) + 1):
        print(nums[i: i + k], nums[i + k: i + (2 * k)])
        if increasing(nums[i: i + k]) and increasing(nums[i + k: i + (2 * k)]):
            return True

    return False


print("Example 1:", hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3))
# print("Example 2:", hasIncreasingSubarrays([2,5,7,2], 3))
# print("Example 3:", hasIncreasingSubarrays([-15,3,16,0], 2))
