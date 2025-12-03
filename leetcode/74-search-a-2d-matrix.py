# 74. Search a 2D Matrix
# Medium

"""
    Intuition:
        can use binary search row wise, by start and end of each row

        considering 2d sorted array as a 1D sorted array
        ROWS, COLS = len(matrix), len(matrix[0])
        lo = 0, hi = (ROWS - 1) * (COLS - 1)


[0, 0] [0, 1] [0, 2]
[1, 0] [1, 1] [1, 2]
[2, 0] [2, 1] [2, 2]
"""


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])

    lo, hi = 0, ROWS * COLS - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        r, c = divmod(mid, COLS)

        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


print(
    "Example 1: ", searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60)
)
