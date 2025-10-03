from typing import List
from heapq import heappop, heappush
def trapRainWater(heightMap: List[List[int]]) -> int:
    ROWS, COLS = len(heightMap), len(heightMap[0])

    min_heap = []

    for r in range(ROWS):
        for c in range(COLS):
            if r in [0, ROWS - 1] or c in [0, COLS - 1]:
                heappush(min_heap, (heightMap[r][c], r, c))
                heightMap[r][c] = -1 # visited

    res = 0
    max_height = -1

    while min_heap:
        h, r, c = heappop(min_heap)
        max_height = max(max_height, h)

        res += max_height - h

        neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

        for nr, nc in neighbors:
            if  (
                nr < 0 or nc < 0 or
                nr == ROWS or nc == COLS or
                heightMap[nr][nc] == -1
            ):
                continue
            heappush(min_heap, (heightMap[nr][nc], nr, nc))
            heightMap[nr][nc] = -1

    return res


print("Example 1", trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))