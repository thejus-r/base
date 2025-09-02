from typing import List
def exist(board: List[List[str]], word:str) -> bool:
    seen = {}

    def notBound(r, c):
        return not (r < len(board) and c < len(board[0]) and r >= 0 and c >= 0)

    def backtrack(r, c, i):
        if i == len(word):
            return True

        if notBound(r, c) or (r, c) in seen:
            return False

        if board[r][c] !=  word[i]:
            i = 0

        if board[r][c] ==  word[i]:
            i += 1


        seen[(r, c)] = True
        return backtrack(r, c + 1, i) or backtrack(r + 1,c, i) or backtrack(r - 1, c, i) or backtrack(r, c -1 , i)

    return backtrack(0,0,0)

print("Example 1: ", exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED" ))
# print("Example 2: ", exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE" ))
# print("Example 3: ", exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))
