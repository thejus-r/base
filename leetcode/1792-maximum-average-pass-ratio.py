# medium
import heapq
from typing import List
def maxAverageRatio(classes: List[List[int]], extraStudents: int) -> float:

    c = len(classes)
    n = extraStudents

    h = []
    def insert(p, t):
        gains = (p + 1) / (t + 1) - (p / t)
        heapq.heappush(h,(-gains, p, t))

    for p, t in classes:
        insert(p, t)

    for _ in range(n):
        _, p, t = heapq.heappop(h)
        insert(p + 1, t + 1)

    total = 0.0
    for _, p, t in h:
        total += p / t

    return total / c

print("Example 1: ", maxAverageRatio([[1,2],[3,5],[2,2]], 2))
