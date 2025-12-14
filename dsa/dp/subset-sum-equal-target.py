# backtracking


import math


def subsetSum(nums: list[int], target: int):
    res = []

    def backtrack(curr: list[int], idx: int, target: int):
        if target == 0:
            res.append(curr.copy())
            return

        if idx == len(nums):
            return

        curr.append(nums[idx])

        backtrack(curr, idx + 1, target - nums[idx])
        curr.pop()

        backtrack(curr, idx + 1, target)

    backtrack([], 0, target)

    return len(res)


# dynamic programming

"""
    Initial DP Array:
                0   1   2   3   4   5  <- sum
     ele -> 0   T   F   F   F   F   F
            1   T   F   F   F   F   F
            2   T   F   F   F   F   F
            3   T   F   F   F   F   F

"""


# Time optimization
# 2D DP Array
# Time Complexity : O((m + 1) (n * 1))
# Space Complexity: O((m + 1) (n * 1))
def subsetSumDP(nums: list[int], target: int) -> bool:
    x = target + 1
    y = len(nums) + 1
    dp = [[False] * x for _ in range(y)]

    for i in range(y):
        dp[i][0] = True

    for i in range(1, y):
        curr_val = nums[i - 1]
        for j in range(1, x):
            if curr_val <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr_val]
            else:
                dp[i][j] = dp[i - 1][j]

    for row in dp:
        print(row)

    return dp[-1][-1]


# Space optimization
# 1D DP Array
# Time Complexity : O((m + 1) (n * 1))
# Space Complexity: O(m + 1)
def subsetSumDPOptimized(nums: list[int], target: int) -> bool:
    x = target + 1
    dp = [False] * x

    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    print(dp)

    return dp[-1]


# Time optimization
# 2D DP Array
# Time Complexity : O((m + 1) (n * 1))
# Space Complexity: O((m + 1) (n * 1))
def countSubSets2(nums: list[int], target: int) -> int:
    x = target + 1
    y = len(nums) + 1

    dp = [[0] * x for _ in range(y)]

    for i in range(y):
        dp[i][0] = 1

    for i in range(1, y):
        curr_sum = nums[i - 1]
        for j in range(1, x):
            if curr_sum <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - curr_sum]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]


# Space optimization
# 1D DP Array
# Time Complexity : O((m + 1) (n * 1))
# Space Complexity: O(m + 1)
def countSubSets3(nums: list[int], target: int) -> int:
    x = target + 1

    dp = [0] * x

    dp[0] = 1

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] + dp[j - num]

    dp[0] = 1
    return dp[-1]


# Minimize the difference of the 2 subsets
def minimumSubsetSum(nums: list[int]) -> int:
    totalSum = sum(nums)

    x = totalSum + 1
    y = len(nums) + 1

    dp = [[False] * x for _ in range(y)]

    for i in range(y):
        dp[i][0] = True

    for i in range(1, y):
        curr_num = nums[i - 1]
        for j in range(1, x):
            if curr_num <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr_num]
            else:
                dp[i][j] = dp[i - 1][j]

    min_sum = float("inf")

    for s, v in enumerate(dp[-1]):
        if v:
            complimentary = totalSum - s
            min_sum = min(min_sum, abs(complimentary - s))

    return int(min_sum)


# Number of Subsets with given difference
# we find the all the possible sums of the subset, the check for the sums that difference
def number_of_subsets_with_diff(nums: list[int], diff: int) -> int:
    target = (diff + sum(nums)) // 2
    x = target + 1
    y = len(nums) + 1

    dp = [[0] * x for _ in range(y)]

    for i in range(y):
        dp[i][0] = 1

    for i in range(1, y):
        curr_num = nums[i - 1]
        for j in range(1, x):
            if curr_num <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - curr_num]
            else:
                dp[i][j] = dp[i - 1][j]

    for row in dp:
        print(row)

    return dp[-1][-1]


print(
    f"Number of Subsets with given difference: {number_of_subsets_with_diff([3, 1, 2, 3], 3)}"
)
