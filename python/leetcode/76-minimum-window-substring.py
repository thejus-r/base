# 76. Minimum Window Substring
# Hard

import sys
from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    needed = defaultdict(int)

    # calculated needed freq
    for char in t:
        needed[char] += 1

    start, end, start_index, min_len, count = 0, 0, 0, sys.maxsize, len(t)

    while end < len(s):
        if needed[s[end]] > 0:
            count -= 1
        needed[s[end]] -= 1
        end += 1

        while count == 0:
            if end - start < min_len:
                start_index = start
                min_len = end - start

            if needed[s[start]] == 0:
                count += 1
            needed[s[start]] += 1
            start += 1

    return "" if min_len == sys.maxsize else s[start_index : start_index + min_len]


# Example 1
s = "ADOBECODEBANC"
t = "ABC"
print("Example 1: ", minWindow(s, t))

# Example 2
s = "a"
t = "a"
print("Example 2: ", minWindow(s, t))

# Example 3
s = "a"
t = "aa"
print("Example 3: ", minWindow(s, t))
