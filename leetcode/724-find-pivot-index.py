def pivotIndex(nums: list[int]) -> int:
    leftSum = nums.copy()
    rightSum = nums.copy()
    n = len(nums)
    for i in range(1, n):
        leftSum[i] += leftSum[i - 1]

    for i in range(n - 2, -1, -1):
        rightSum[i] += rightSum[i + 1]

    for i in range(0, n):
        if leftSum[i] == rightSum[i]:
            return i

    return -1



print("Example 1: ", pivotIndex([1, 7, 3, 6, 5, 6])) # 3
print("Example 2: ", pivotIndex([1, 2, 3])) # -1
print("Example 3: ", pivotIndex([2, 1, -1])) # 0
