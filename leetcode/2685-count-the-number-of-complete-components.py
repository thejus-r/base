# 2685. Count the Number of Complete Components
# Medium

from collections import defaultdict


# using dfs
def countCompleteComponents(n: int, edges: list[list[int]]) -> int:
    res = 0
    visit = set()

    adj = defaultdict(list)
    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)

    def dfs(v, res: list[list[int]]):
        if v in visit:
            return res

        visit.add(v)

        res.append(v)
        for nei in adj[v]:
            dfs(nei, res)

        return res

    for v in range(n):
        if v in visit:
            continue
        component = dfs(v, [])
        if all([len(component) - 1 == len(adj[v2]) for v2 in component]):
            res += 1

    return res


print("Example 1: ", countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]]))
# print( "Example 2: ", countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]))
