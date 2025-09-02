from typing import List
def numberOfPairs(points: List[List[int]]) -> int:
    N = len(points)
    count = 0
    for i in range(N):
        ax, ay = points[i]
        for j in range(N):
            if i == j:
                continue # same points, not to be taken
            bx, by = points[j]

            if not (by >= ay and bx <= ax):
                continue

            found = False
            for k in range(N):
                if k == i or k == j:
                    continue
                cx, cy = points[k]
                if bx <= cx <= ax and by >= cy >= ay:
                    found = True
            if not found:
                count += 1
    return count


print("Example 1:", numberOfPairs([[1,1],[2,2],[3,3]])) # 0
print("Example 2:", numberOfPairs([[6,2],[4,4],[2,6]])) # 2
print("Example 3:", numberOfPairs([[3,1],[1,3],[1,1]])) # 2
