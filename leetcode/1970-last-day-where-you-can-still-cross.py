# 1970. Last Day Where You Can Still Cross
# Hard


from collections import deque
from typing import Deque, Tuple


def latestDayToCross(row: int, col: int, cells: list[list[int]]) -> int:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def can_cross(day: int):
        # initialize grid
        grid = [[0] * col for _ in range(row)]

        # apply transitions till day
        for i in range(day):
            cx, cy = cells[i]
            grid[cx - 1][cy - 1] = 1

        q: Deque[Tuple[int, int]] = deque()
        for i in range(len(grid[0])):
            if grid[0][i] == 0:
                q.append((0, i))

        seen = set()
        while q:
            x, y = q.popleft()

            # base case, we have reached bottom
            if x == row - 1:
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < row
                    and 0 <= ny < col
                    and (nx, ny) not in seen
                    and grid[nx][ny] == 0
                ):
                    seen.add((nx, ny))
                    q.append((nx, ny))
        return False

    lo, hi = 1, len(cells) - 1
    ans = 0

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if can_cross(mid):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return ans


row, col = 2, 2
cells = [[1, 1], [2, 1], [1, 2], [2, 2]]
print(f"Example 1: {latestDayToCross(row, col, cells)}")

row, col = 2, 2
cells = [[1, 1], [1, 2], [2, 1], [2, 2]]
print(f"Example 2: {latestDayToCross(row, col, cells)}")

row, col = 3, 3
cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
print(f"Example 3: {latestDayToCross(row, col, cells)}")

row, col = 2, 6
cells = [ [1, 4], [1, 3], [2, 1], [2, 5], [2, 2], [1, 5], [2, 4], [1, 2], [1, 6], [2, 3], [2, 6], [1, 1], ]  # fmt:skip
print(f"Example 5: {latestDayToCross(row, col, cells)}")
