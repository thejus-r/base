# 416. Partition Equal Subset Sum
# Medium


def canPartition(nums: list[int]) -> bool:
    s = sum(nums)

    # short-circuit: if sum is not even
    if s % 2 != 0:
        return False

    target = s // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        print(dp)
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[-1]


print(f"Example 1: {canPartition([1, 5, 11, 5])}")
print(f"Example 2: {canPartition([3, 3, 3, 4, 5])}")
