from typing import List
def numberOfPairs(points: List[List[int]])  -> int:
    points.sort(key=lambda p: (p[0], -p[1]))
    n = len(points)
    ans = 0

    for i in range(n):
        pointA = points[i]
        yMax = -float('inf')

        for j in range(i + 1, n):
            pointB = points[j]

            if pointA[1] >= pointB[1]:
                if pointB[1]> yMax:
                    ans += 1
                    yMax = pointB[1]

    return ans

print( "Example 1", numberOfPairs([[1,1],[2,2],[3,3]]))
print( "Example 2", numberOfPairs([[6,2],[4,4],[2,6]]))
print( "Example 3", numberOfPairs([[3,1],[1,3],[1,1]]))
