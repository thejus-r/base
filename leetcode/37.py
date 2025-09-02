# Leetcode: 37
# Suduko Solver
# https://leetcode.com/problems/suduko-solver
# hard

import collections
from typing import  List
def solveSudoko(board: List[List[str]]):
    n = len(board)
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(n):
        for c in range(n):
            if board[r][c] == ".":
                continue
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    def backtrack(r,c):
        # base case
        if r == n:
            return True

        # when only c reached 9, move to next row and col 0
        if c == n:
            return backtrack(r + 1, 0)

        if board[r][c] != ".":
            return backtrack(r, c + 1)

        for i in range(1, 10):
            d = str(i)
            if d not in rows[r] and d not in cols[c] and d not in squares[(r//3, c//3)]:
                rows[r].add(d)
                cols[c].add(d)
                squares[(r//3, c//3)].add(d)
                board[r][c] = d
                if backtrack(r, c+ 1):
                    return True
                rows[r].remove(d)
                cols[c].remove(d)
                squares[(r//3, c//3)].remove(d)
                board[r][c] = "."
        return False
    backtrack(0,0)

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoko(board)
print(board)
