from typing import List
def number_of_pairs(points: List[List[int]])  -> int:
    count = 0
    n = len(points)
    for i in range(n):
        ax, ay = points[i]
        for j in range(n):
            if i == j:
                continue
            bx, by = points[j]
            if not (ax <= bx and ay >= by):
                continue
            found = False
            for k in range(n):
                if k == i or j == k:
                    continue
                cx, cy = points[k]
                if ax <= cx <= bx and ay >= cy >= by:
                    found = True
            if not found:
                count+= 1

    return count

print( "Example 1", number_of_pairs([[1,1],[2,2],[3,3]]))
print( "Example 2", number_of_pairs([[6,2],[4,4],[2,6]]))
print( "Example 3", number_of_pairs([[3,1],[1,3],[1,1]]))
