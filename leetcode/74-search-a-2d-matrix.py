from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    l, r = 0, ROWS * COLS - 1
    while l <= r:
        m = l + (r - l) // 2
        row, col = m // COLS, m % COLS
        if matrix[row][col] < target:
            l = m + 1
        elif matrix[row][col] > target:
            r = m - 1
        else:
            return True

    return False

print(f"Example 1:", searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
print(f"Example 1:", searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 2)) # False