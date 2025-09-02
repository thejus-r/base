# easy

def isAnagram(s: str, t: str) -> bool:
    if (len(s) != len(t)): return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for value in count:
        if value != 0:
            return False

    return True

print("Example 1: ", isAnagram("anagram", "nagaram"))
print("Example 1: ", isAnagram("rat", "car"))
