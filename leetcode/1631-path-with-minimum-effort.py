from heapq import heappop, heappush
from typing import List
def minimumEffortPath(heights: List[List[int]]) -> int:
    ROWS, COLS = len(heights), len(heights[0])

    minHeap = [[0, 0, 0]] # [diff, r, c]
    visit = set()

    directions = [[ 0, 1 ], [1, 0], [-1, 0], [0, -1]]

    while minHeap:
        diff, r, c = heappop(minHeap)
        if (r, c) in visit:
            continue
        visit.add((r, c))

        if (r, c) == (ROWS - 1, COLS - 1):
            return diff

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                nr < 0 or nc < 0 or nc == COLS or nr == ROWS or (nr, nc) in visit
            ):
                continue

            newDiff = max(abs(heights[nr][nc] - heights[r][c]), diff)
            heappush(minHeap, [newDiff, nr, nc])

    return 0

heights = [[1,2,2],[3,8,2],[5,3,5]]
print(f"Example 1: {minimumEffortPath(heights)}")

heights = [[1,2,3],[3,8,4],[5,3,5]]
print(f"Example 2: {minimumEffortPath(heights)}")

heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(f"Example 3: {minimumEffortPath(heights)}")