# 696. Count Binary Substrings
# Easy

def countBinarySubstrings(s: str) -> int:
    groups = [1]
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            groups.append(1)
        else:
            groups[-1] += 1

    ans = 0


    for i in range(1, len(groups)):
        ans += min(groups[i], groups[i - 1])

    return ans

print("Example 1: ", countBinarySubstrings("00110011")) # 6c