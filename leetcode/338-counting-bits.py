# 338. Counting Bits
# Easy

def countBits(n: int) -> list[int]:
    dp: list[int] = [0] * (n + 1)
    sub = 1

    for i in range(1, n + 1):
        if sub * 2 == i:
            sub = i
        dp[i] = dp[i - sub] + 1

    return dp


print("Example 1: ", countBits(2))
print("Example 2: ", countBits(5))
