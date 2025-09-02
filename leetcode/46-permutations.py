from typing import List
def permute(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans, sol = [], []

    def backtrack():
        if len(sol) == n:
            ans.append(sol[:])
            return
        for x in nums:
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()
    backtrack()
    return ans

print("Example 1:", permute([1,2,3]))
print("Example 2:", permute([0,1]))
