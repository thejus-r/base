# 1422. Maximum Score After Splitting a String
# Easy

def maxScore(s: str) -> int:
    ones = 0
    zeros = 0
    best = -float("inf")

    for i in range(len(s) - 1):
        if s[i] == "1":
            ones += 1
        else:
            zeros += 1

        best = max(best, zeros - ones)
        print(ones, zeros, best)

    if s[-1] == "1":
        ones += 1

    return int(best + ones)



print("Example 1: ", maxScore("011101"))
# print("Example 2: ", maxScore("00111"))
# print("Example 3: ", maxScore("1111"))
