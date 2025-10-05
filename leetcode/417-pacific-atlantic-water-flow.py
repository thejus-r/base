import collections
from typing import List
from heapq import heappush, heappop
def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    R, C = len(heights), len(heights[0])
    res = []

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    def bfs(start):
        q = collections.deque()
        possible = set()

        for x, y in start:
            q.append((x, y))
            possible.add((x, y))

        while len(q) > 0:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in possible and heights[nx][ny] >= heights[x][y]:
                    q.append((nx, ny))
                    possible.add((nx, ny))

        return possible

    pacific, atlantic = [], []
    for i in range(R):
        pacific.append((i, 0))
        atlantic.append((i, C - 1))

    for i in range(C):
        pacific.append((0, i))
        atlantic.append((R - 1, i))

    p = bfs(pacific)
    a = bfs(atlantic)

    return list(sorted(p & a))

print(f"Example 1: ", pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))