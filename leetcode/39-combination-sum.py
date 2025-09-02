# medium
from typing import List
def combinationSub(canditates: List[int], target: int) -> List[List[int]]:
    res = []

    def backtrack(i, curr, total):
        if target == total:
            res.append(curr.copy())
            return
        if total > target or i > len(canditates) - 1:
            return

        curr.append(canditates[i])
        backtrack(i, curr, total + canditates[i])
        curr.pop()
        backtrack(i + 1, curr, total)


    backtrack(0, [], 0)
    return res

print("Example 1:", combinationSub([2,3,6,7], 7))
print("Example 2:", combinationSub([2,3,5], 8))
print("Example 3:", combinationSub([2], 1))
