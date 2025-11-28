'''
intuition:
    - actual values doesnt matter
    - we can do a dfs or a dp array to keep the state
    - how to keep state tho? still needs to be found

    - can use a 3D DP array to store the state
    - trying bottom up approach

'''
def numberOfPaths(grid: list[list[int]], k: int) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    MOD = 10 ** 9 + 7

    dp = [[[0] * k for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

    target_reminder = (k - (grid[ROWS - 1][COLS - 1] % k )) % k

    dp[ROWS - 1][COLS - 1][target_reminder] = 1

    for r in reversed(range(ROWS)):
        for c in reversed(range(COLS)):

            # Skipping the initial value
            if r == ROWS - 1 and c == COLS - 1:
                continue

            for remain in range(k):
                new_remain = (remain + grid[r][c]) % k
                dp[r][c][remain] = (
                    dp[r + 1][c][new_remain] % MOD + 
                    dp[r][c + 1][new_remain] % MOD
                    ) % MOD

    return dp[0][0][0]

# print("Example 1: ", numberOfPaths([[5,2,4],[3,0,5],[0,7,2]], 3))
print("Example 2: ", numberOfPaths([[7,3,4,9],[2,3,6,2],[2,3,7,0]], 3))

