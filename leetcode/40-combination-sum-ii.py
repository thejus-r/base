from typing import List
def combinationSum2(candidates: List[int], target: int)-> List[List[int]]:
    res = []
    candidates.sort()

    def backtrack(i, curr, total):
        if total == target:
            res.append(curr.copy())
            return
        if total > target or i == len(candidates):
            return

        curr.append(candidates[i])
        backtrack(i + 1, curr, total + candidates[i])
        curr.pop()

        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        backtrack(i + 1, curr, total)

    backtrack(0, [], 0)
    return res

print("Example 1:", combinationSum2([10,1,2,7,6,1,5], 8))
print("Example 1:", combinationSum2([2,5,2,1,2], 5))
