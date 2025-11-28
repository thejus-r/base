# 323. Number of Connected Components in an Undirected Graph
# Medium


from collections import defaultdict


def countComponents(n: int, edges: list[list[int]]) -> int:
    # build adj list
    adj = defaultdict(list)

    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)

    res = 0
    visited = set()

    # dfs to find the components
    def dfs(v, res):
        if v in visited:
            return
        visited.add(v)
        res.append(v)

        for nei in adj[v]:
            dfs(nei, res)

        return res

    for v in range(n):
        if v in visited:
            continue
        res += 1
        dfs(v, [])

    return res


print("Example 1: ", countComponents(3, [[0, 1], [0, 2]]))
print("Example 2: ", countComponents(6, [[0, 1], [1, 2], [2, 3], [4, 5]]))
