from collections import Counter, deque
from typing import List
from heapq import heapify, heappop, heappush

# for scheduling a task we can use a pHeap and Queue
def leastInterval(tasks: List[str], n: int) -> int:
    time, q = 0, deque()
    maxHeap = [-cnt for cnt in Counter(tasks).values()]
    heapify(maxHeap)

    while q or maxHeap:
        time += 1
        if maxHeap:
            cnt = 1 + heappop(maxHeap)
            if cnt:
                q.append([cnt, time + n])
        if q and q[0][1] == time:
            heappush(maxHeap, q.popleft()[0])
    return time

print(f"Example 1: {leastInterval(["A","A","A","B","B","B"], 2)}") # 8
print(f"Example 2: {leastInterval(["A","C","A","B","D","B"], 1)}") # 6
print(f"Example 3: {leastInterval(["A","A","A", "B","B","B"], 3)}") # 10