from collections import deque
from heapq import heappop, heappush
from typing import List

# Combination of 2 problems 1 Medium and 1 Hard
# Hard -> Swim in Rising Water, Medium -> Walls and Gates

def maximumSafenesFactor(grid: List[List[int]]) -> int:
    n = len(grid)

    # helper
    def isValidCell(r, c):
        return 0 <= r < n and 0 <= c < n

    def precompute():
        q = deque()
        min_dist = {}
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    q.append([r, c, 0])
                    min_dist[(r, c)] = 0
        while q:
            r, c, dist = q.popleft()
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                if isValidCell(nr, nc) and (nr, nc) not in min_dist:
                    min_dist[(nr, nc)] = dist + 1
                    q.append([nr, nc, dist + 1])
        return min_dist

    min_dist = precompute()
    maxHeap = [(-min_dist[(0, 0)], 0, 0)]
    visit = set()
    visit.add((0, 0))
    while maxHeap:
        dist, r, c = heappop(maxHeap)
        dist = -dist
        if (r, c) == (n - 1, n - 1):
            return dist
        neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
        for nr, nc in neighbors:
            if isValidCell(nr, nc) and (nr, nc) not in visit:
                visit.add((nr, nc))
                newDist = min(dist, min_dist[(nr, nc)])
                heappush(maxHeap, (-newDist, nr, nc))
    return -1

grid = [[1,0,0],[0,0,0],[0,0,1]]
print(f"Example 1: {maximumSafenesFactor(grid)}") # 0


grid = [[0,0,1],[0,0,0],[0,0,0]]
print(f"Example 2: {maximumSafenesFactor(grid)}") # 2


grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
print(f"Example 3: {maximumSafenesFactor(grid)}") # 2