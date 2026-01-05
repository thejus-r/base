# 1975. Maximum Matrix Sum
# Medium


def maxMatrixSum(matrix: list[list[int]]) -> int:
    totalSum = 0
    negCount = 0
    min_abs_val = float("inf")

    for row in matrix:
        for val in row:
            totalSum += abs(val)
            if val < 0:
                negCount += 1
            min_abs_val = min(min_abs_val, abs(val))

    if negCount % 2 != 0:
        totalSum -= min_abs_val * 2
    return int(totalSum)


matrix = [[1, -1], [-1, 1]]
print(f"Example 1: {maxMatrixSum(matrix)}")

matrix = [[1, 2, 3], [-1, -2, -3], [1, 2, 3]]
print(f"Example 2: {maxMatrixSum(matrix)}")

matrix = [[-1, 0, -1], [-2, 1, 3], [3, 2, 2]]
print(f"Example 3: {maxMatrixSum(matrix)}")
