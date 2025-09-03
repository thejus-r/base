from test.re_tests import u
from typing import List
def permuteUnique(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res, sol = [], []
    count = { n:0 for n in nums }

    for n in nums:
        count[n] += 1

    def dfs():
        if len(sol) == len(nums):
            res.append(sol[:])
            return
        for n in count:
            if count[n] > 0:
                sol.append(n)
                count[n] -= 1

                dfs()

                count[n] += 1
                sol.pop()

    dfs()
    return res

print("Example 1: ", permuteUnique([1,1,2]))
print("Example 1: ", permuteUnique([1,2,3]))
