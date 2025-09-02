# Leetcode: 52
# N-Queens II
# https://leetcode.com/problems/n-queens-ii
# hard

def solvedQueens(n: int) -> int:
    cols = set()
    negDiag = set() # r - c
    posDiag = set() # r + c

    res = 0
    def backtrack(r):
        if r == n:
            nonlocal res
            res += 1
            return
        for c in range(n):
            if c in cols or (r- c) in negDiag or (r+c) in posDiag:
                continue
            cols.add(c)
            negDiag.add(r - c)
            posDiag.add(r + c)
            backtrack(r + 1)
            cols.remove(c)
            negDiag.remove(r - c)
            posDiag.remove(r + c)
    backtrack(0)
    return res


print("Example 1:", solvedQueens(4))
print("Example 2:", solvedQueens(1))
