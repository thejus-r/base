'''
intuition:
    - actual values doesnt matter
    - we can do a dfs or a dp array to keep the state
    - how to keep state tho? still needs to be found
    

'''
def numberOfPaths(grid: list[list[int]], k: int) -> int:
    mod = 10 ** 9 + 7

    rows, cols = len(grid), len(grid[0])

    # this is for number of paths
    count = 0

    # dp array: initalized all zeros
    dp = [[0] * cols for _ in range (rows)]

    # pre-process: finding the reminder of all, may be not nessasory
    for i in range (rows):
        for j in range(cols):
            grid[i][j] %= k

    # depth first search to find the possible paths

    print(grid)
    print(dp)

    return 0

print("Example 1: ", numberOfPaths([[5,2,4],[3,0,5],[0,7,2]], 3))
# print("Example 2: ", numberOfPaths([[7,3,4,9],[2,3,6,2],[2,3,7,0]], 3))

