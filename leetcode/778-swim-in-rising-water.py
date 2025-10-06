from heapq import heappop, heappush
from typing import List

def swimInWater(grid: List[List[int]]) -> int:
    N = len(grid)
    minHeap = []
    visited = set()

    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    heappush(minHeap, [grid[0][0], 0, 0])
    visited.add((0,0))

    while minHeap:
        t, r, c = heappop(minHeap)
        if r == N - 1 and c == N - 1:
            return t

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                visited.add((nr,nc))
                heappush(minHeap, [max(t, grid[nr][nc]), nr, nc])

    return N * N - 1

grid = [[0,2],[1,3]]
print(f"Example 1: {swimInWater(grid)}") # 3

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(f"Example 2: {swimInWater(grid)}") # 16