# 3. Longest Substring Without Repeating Characters
# Medium


def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    left = 0
    seen = {}

    for right, c in enumerate(s):
        if c in seen and seen[c] >= left:
            left = seen[c] + 1

        max_len = max(max_len, right - left + 1)
        seen[c] = right

    return max_len


print("Example 1: ", lengthOfLongestSubstring("aab"))  # 2
print("Example 2: ", lengthOfLongestSubstring("abcabcbb"))  # 3
print("Example 3: ", lengthOfLongestSubstring("bbbbb"))  # 1
print("Example 4: ", lengthOfLongestSubstring("abba"))  # 2
