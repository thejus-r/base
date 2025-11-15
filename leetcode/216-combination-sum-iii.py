# 216. Combination Sum III
# Medium

"""
intuition:
    - combinations of length k, that sums to n
    - can use backtack tracking to create combination that works
    - use target var, when target reaches 0, we have found combination
    - if target goes less than zero, not possible
"""


def combinationSum3(k: int, n: int) -> list[list[int]]:
    res: list[list[int]] = []

    def backtrack(curr, i, target):
        if len(curr) > k or target > n or i > 9:
            return
        if len(curr) == k and target == n:
            res.append(curr.copy())
            return

        i = i + 1
        curr.append(i)
        backtrack(curr, i, target + i)
        curr.pop()
        backtrack(curr, i, target)

    backtrack([], 0, 0)
    return res


# print("Example 1: ", combinationSum3(3, 7))
# print("Example 2: ", combinationSum3(3, 9))
print("Example 2: ", combinationSum3(9, 45))
