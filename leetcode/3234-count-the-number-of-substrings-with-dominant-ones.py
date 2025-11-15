# 3234. Count the Number of Substrings With Dominant Ones
# Medium

def numberOfSubstrings(s:str) -> int:
    n = len(s)
    pre = [0] * (n + 1)

    for i in range(n):
        if s[i] == "0":
            pre[i + 1] = i + 1
        else:
            pre[i + 1] = pre[i]
    res = 0

    for i in range(1, n + 1):
        j = i
        cnt0 = 0
        while j > 0 and cnt0 * cnt0 <= n:
            cnt1 = i - pre[j] - cnt0
            if cnt1 >= cnt0 * cnt0:
                prev_j = pre[j]
                res += min(j - prev_j, cnt1 - cnt0 * cnt0 + 1)
            j = pre[j]
            cnt0 += 1
    return res

print("Example 1: ", numberOfSubstrings("00011"))






