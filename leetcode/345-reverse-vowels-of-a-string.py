# 345. Reverse Vowels of a String
# Easy

def reverseVowels(s: str) -> str:
    arr = list(s)
    left, right = 0, len(arr) - 1
    vowels = "aeiou"

    while left < right:
        while left < right and arr[left].lower() not in vowels:
            left += 1

        while left < right and arr[right].lower() not in vowels:
            right -= 1

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return "".join(arr)


print("Example 1: ", reverseVowels("IceCreAm"))
print("Example 2: ", reverseVowels("leetcode"))
