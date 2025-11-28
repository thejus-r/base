# 261. Graph Valid Tree
# Medium

"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether these
edges make up a valid tree.
"""

from collections import defaultdict


def validTree(n: int, edges: list[list[int]]) -> bool:
    if not n:
        return True

    # build adj list
    adj = defaultdict(list)

    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)

    visited = set()

    def dfs(v, prev):
        if v in visited:
            return False
        visited.add(v)

        for nei in adj[v]:
            if nei == prev:
                continue
            if not dfs(nei, v):
                return False
        return True

    return dfs(0, -1) and n == len(visited)


print("Example 1: ", validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print("Example 2: ", validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
