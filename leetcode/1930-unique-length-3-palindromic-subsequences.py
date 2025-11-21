def countPalindromeSubsequence(s: str) -> int:
    letters = set(s)
    ans = 0

    for letter in letters:
        i, j = s.index(letter), s.rindex(letter)
        between = set()

        for k in range(i + 1, j):
            between.add(s[k])
        ans += len(between)

    return ans


print("Example 1:", countPalindromeSubsequence("aabca"))
print("Example 2:", countPalindromeSubsequence("adc"))
print("Example 3:", countPalindromeSubsequence("bbcbaba"))
