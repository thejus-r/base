from typing import List

# BruteForce: O(N^2)
def maxArea1(height: List[int]) -> int:
    n = len(height)
    maxArea = 0

    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            maxArea = max(maxArea, area)
    return maxArea

def maxArea2(height: List[int]) -> int:
    res = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res




print(f"Example 1 (bruteforce): {maxArea1([1,8,6,2,5,4,8,3,7])}")
print(f"Example 2 (two-pointers): {maxArea1([1,8,6,2,5,4,8,3,7])}")