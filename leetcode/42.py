# Leetcode: 42
# Trapping Rain water
# https://leetcode.com/problems/trapping-rain-water
# hard

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while (l < r):
            if (leftMax < rightMax):
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res

sol = Solution()
print("Example 1:", sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print("Example 2:", sol.trap([4,2,0,3,2,5]))
