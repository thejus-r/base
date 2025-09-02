# Leetcode: 48
# Rotate Image
# https://leetcode.com/problems/rotate-image
# medium

from typing import List
def rotate(matrix: List[List[int]]) -> None:
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            topLeft = matrix[top][l + i]

            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = topLeft
        r -= 1
        l += 1


rotate([[1,2,3],[4,5,6],[7,8,9]])
