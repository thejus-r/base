# for weighted directed graph
from typing import Dict, List
from heapq import heappop, heappush
def shortestPath(n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
    adj = {}

    for i in range(n):
        adj[i] = []

    for s, d, weight in edges:
        adj[s].append([d, weight])

    print(adj)

    shortest = {} # Map Vertex -> dist of shortest path
    minHeap = [[0, src]]

    while minHeap:
        w1, n1 = heappop(minHeap)
        if n1 in shortest:
            continue
        shortest[n1] = w1

        for n2, w2 in adj[n1]:
            if n2 not in shortest:
                heappush(minHeap, [w1 + w2, n2])

    for i in range(n):
        if i not in shortest:
            shortest[i] = -1

    return shortest

n = 5
edges = [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]] # [source, destination, weight]
src = 0
print("Example 1: ", shortestPath(n, edges, src))
# Example 1:  {0: 0, 2: 3, 4: 5, 1: 7, 3: 9}