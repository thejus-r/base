# 3607. Power Grid Maintenance
# Medium


from collections import defaultdict
from heapq import heappop, heappush


def processQueries(
    c: int, connections: list[list[int]], queries: list[list[int]]
) -> list[int]:
    ans: list[int] = []

    adj = defaultdict(list)
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)

    online: set[int] = set()
    station_group = {}
    min_heaps = defaultdict(list)

    def dfs(station, group_id):
        if station in online:
            return
        online.add(station)
        station_group[station] = group_id
        heappush(min_heaps[group_id], station)

        for nei in adj[station]:
            dfs(nei, group_id)

    for s in range(1, c + 1):
        dfs(s, s)

    for q_type, q_station in queries:
        if q_type == 1:
            if q_station in online:
                ans.append(q_station)
                continue
            group_id = station_group[q_station]
            min_heap = min_heaps[group_id]

            while min_heap and min_heap[0] not in online:
                heappop(min_heap)

            if min_heap:
                ans.append(min_heap[0])
            else:
                ans.append(-1)

        else:
            online.discard(q_station)

    return ans


print(
    "Example 1: ",
    processQueries(
        5, [[1, 2], [2, 3], [3, 4], [4, 5]], [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]
    ),
)
