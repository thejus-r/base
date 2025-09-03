from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.sumMatrix = matrix
        for i in range(0, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.sumMatrix[i][j] = self.sumMatrix[i][j - 1] + self.sumMatrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        if col1 == 0:
            for i in range(row1, row2 + 1):
                sum += self.sumMatrix[i][col2]
            return sum

        for i in range(row1, row2 + 1):
            sum += self.sumMatrix[i][col2] - self.sumMatrix[i][col1 - 1]


        return sum


mat = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(mat.sumRegion(2,1,4,3)) # 8
print(mat.sumRegion(1,1,2,2)) # 11
print(mat.sumRegion(1,2,2,4)) # 12
