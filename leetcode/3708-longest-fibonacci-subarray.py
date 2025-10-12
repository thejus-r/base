# 3708. Longest Fibonacci Subarray
# Medium

'''
intuition:
    can use two pointers to track the length of the fib sequence
    third and subsequent terms each equal the sum of the two preceding terms
'''

def longestSubarray(nums: list[int]) -> int:
    n = len(nums)
    if n <= 2:
        return n

    ans, c = 2, 2
    for i in range(2, n):
        if nums[i] == nums[i - 1] + nums[i - 2]:
            c += 1
        else:
            c = 2

        ans = max(ans, c)
    return ans

print("Example 1:", longestSubarray([1,1,1,1,2,3,5,1])) # 5
print("Example 2:", longestSubarray([5,2,7,9,16])) # 5
