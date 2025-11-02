from functools import cache


def countUnguarded(
    m: int, n: int, guards: list[list[int]], walls: list[list[int]]
) -> int:
    """
    intuition
    1. Walls block the guards vision
    2. Guards can see from end to end
    3. Guards can see all directions (E, W, N, S)

    can have dp array: setting all as '1'
    loop through all guards.. find all guarded spots
    """
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # setting all cells to 1 (safe)
    dp = [[1 for _ in range(n)] for _ in range(m)]

    # setting walls as 0 (unsafe)
    for x, y in guards:
        dp[x][y] = 0

    # setting walls as -1
    for x, y in walls:
        dp[x][y] = -1

    @cache
    def dfs(r: int, c: int, dr: int, dc: int):
        # check for boundary
        if r == -1 or r == m or c == -1 or c == n:
            return

        if dp[r][c] == -1:
            return

        dp[r][c] = 0
        nr, nc = r + dr, c + dc
        dfs(nr, nc, dr, dc)

    for r, c in guards:
        for dr, dc in directions:
            dfs(r, c, dr, dc)

    count = 0
    for i in range(m):
        for j in range(n):
            if dp[i][j] == 1:
                count += 1

    return count


print(
    "example 1",
    countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]),
)

print(
    "example 2",
    countUnguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]),
)
