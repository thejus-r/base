# 392. Is Subsequence
# Easy
def isSubsequence(s: str, t: str) -> bool:
    # preprocess
    nxt:list[dict[str, int]] = [{} for _ in range(len(t) + 1)]
    for i in range(len(t) - 1, -1 , -1):
        nxt[i] = nxt[i + 1].copy()
        nxt[i][t[i]] = i + 1

    i = 0
    for c in s:
        if c in nxt[i]:
            i = nxt[i][c]
        else:
            return False
    return True

# print("Example 1:", isSubsequence("abc", "ahbgdc"))
# print("Example 2:", isSubsequence("axc", "ahbgdc"))
# print("Example 3:", isSubsequence("", "ahbgdc"))
# print("Example 4:", isSubsequence("b", "c"))
print("Example 5:", isSubsequence("bcd", "uuuubcd"))
