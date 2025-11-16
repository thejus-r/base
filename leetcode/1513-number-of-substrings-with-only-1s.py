# 1513. Number of Substrings With Only 1s
# Medium


def numSub(s: str) -> int:
    group = 0
    res = 0
    for i in range(len(s)):
        if s[i] == "0":
            res += group * (group + 1) // 2
            group = 0
        else:
            group += 1

    res += group * (group + 1) // 2
    res %= 10**9 + 7
    return res


print("Example 1: ", numSub("0110111"))
print("Example 2: ", numSub("101"))
print("Example 3: ", numSub("111111"))
