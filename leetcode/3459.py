# Leetcode: 3459
# Length of Longest V-Shaped Diagonal Segment
# https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment
# #hard

# Should Start with 1
# Direction Rotation of Segment -> Clock-wise
# After "1" Sequence Should be "20202..."
# Can't go out of boundary <- basecase
# has already done 1 rotation <- basecase
# not in subsequence <- basecase

import functools
from typing import List

def longestVShapedSegment(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    DIRS = [(-1, 1), (1,1), (1,-1), (-1,-1)] # TR, BR, BL, TL

    @functools.cache
    def dfs(x, y, direction, turn, target):
        if not (0 <= x < n and 0<= y < m and grid[x][y] == target):
            return 0

        nx, ny = x + DIRS[direction][0], y + DIRS[direction][1]
        max_step = 1 + dfs(nx, ny, direction, turn, 2-target)

        if (turn == 0):
            nd = (direction + 1) % 4
            nx, ny = x + DIRS[nd][0], y + DIRS[nd][1]
            max_step = max(max_step, 1 + dfs(nx, ny, nd, 1, 2-target))
        return max_step

    res  = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                max_len = 0
                for d in range(4):
                    nx, ny = i + DIRS[d][0], j + DIRS[d][1]
                    max_len = max(max_len, 1 + dfs(nx, ny, d, 0, 2))
                res = max(res, max_len)
    return res

print("Example 1: ",longestVShapedSegment(
    [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
))

print("Example 2: ",longestVShapedSegment(
    [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
))

print("Example 3: ",longestVShapedSegment(
    [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
))

print("Example 4: ",longestVShapedSegment(
    [[1]]
))
