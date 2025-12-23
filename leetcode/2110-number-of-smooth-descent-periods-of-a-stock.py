# 2110. Number of Smooth Descent Periods of a Stock
# Medium


def getDescentPeriods(prices: list[int]) -> int:
    ans = 1
    cnt = 1

    for i in range(1, len(prices)):
        if prices[i] == prices[i - 1] - 1:
            cnt += 1
        else:
            cnt = 1
        ans += cnt

    return ans


print("Example 1: ", getDescentPeriods([3, 2, 1, 4]))
print("Example 2: ", getDescentPeriods([8, 6, 7, 7]))
print("Example 3: ", getDescentPeriods([1]))
print(
    "Example 4: ",
    getDescentPeriods([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 4, 3, 10, 9, 8, 7]),
)
