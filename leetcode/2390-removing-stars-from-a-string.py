# 2390. Removing Stars From a String
# Medium

from collections import deque


def removeStars(s: str) -> str:
    stack = deque()

    for c in s:
        if c == "*":
            stack.popleft()
        else:
            stack.appendleft(c)

    return "".join(stack)[::-1]


print("Example 1:", removeStars("leet**cod*e"))
