# Leetcode: 3446
# Sort Matrix by Diagonals
# https://leetcode.com/problems/sort-matrix-by-diagonals
# medium
import heapq
from typing import List
def sortMatrix(grid: List[List[int]]) -> List[List[int]]:
    heap = []
    heapq.heapify(heap)
    n = len(grid)
    ## sort bottom left triangle
    for i in range (0, n):
        x, y = i, 0
        for j in range(0, n - i):
            heapq.heappush(heap, -grid[x][y])
            x, y = x + 1, y + 1
        x, y = i, 0
        for j in range(0, n - i):
            grid[x][y] = -heapq.heappop(heap)
            x, y = x + 1, y + 1

    ## sort top right triangle
    for i in range (1, n):
        x, y = 0, i
        for j in range(0, n - i):
            heapq.heappush(heap, grid[x][y])
            x, y = x + 1, y + 1
        x, y = 0, i
        for j in range(0, n - i):
            grid[x][y] = heapq.heappop(heap)
            x, y = x + 1, y + 1

    return grid

print("Example 1: ", sortMatrix(
    [[1,7,3],[9,8,2],[4,5,6]]
))

print("Example 2: ", sortMatrix(
    [[0,1],[1,2]]
))

print("Example 3: ", sortMatrix(
    [[1]]
))
