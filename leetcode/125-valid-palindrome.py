# 125. Valid Palindrome
# Easy
def isPalindrome(s: str) ->  bool:
    newStr = ""
    # pre process
    for ch in s:
        if ch.isalnum():
            newStr += ch.lower()

    left, right = 0, len(newStr) -1
    while left <= right:
        if newStr[left] == newStr[right]:
            left += 1
            right -= 1
        else:
            return False


    return True

print("Example 1: ", isPalindrome("A man, a plan, a canal: Panama"))
print("Example 2: ", isPalindrome("race a car"))
