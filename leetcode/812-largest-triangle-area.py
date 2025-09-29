from typing import List
def largestTriangleArea(points: List[List[int]]) -> float:
    max_area = float("-inf")

    for x1, y1 in points:
        for x2, y2 in points:
            for x3, y3 in points:
                currArea = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                max_area = max(max_area, currArea)

    return max_area

print("Example 1: ", largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
print("Example 2: ", largestTriangleArea([[1,0],[0,0],[0,1]]))