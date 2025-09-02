# Leetcode: 621
# Task Scheduler
# https://leetcode.com/problems/task-scheduler
# medium

from heapq import heapify, heappush, heappop
from collections import deque
from typing import List
from collections import Counter
def leastInterval(tasks: List[str], n: int) -> int:
    time, q = 0, deque()
    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapify(maxHeap)

    while maxHeap or q:
        time += 1

        if maxHeap:
            cnt = 1 + heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
        if q and q[0][1] == time:
            heappush(maxHeap, q.popleft()[0])

    return time


print("Example 1:", leastInterval(["A","A","A","B","B","B"],2)) # 8
print("Example 2:", leastInterval(["A","C","A","B","D","B"],1)) # 6
print("Example 3:", leastInterval(["A","A","A","B","B","B"],3)) # 10
