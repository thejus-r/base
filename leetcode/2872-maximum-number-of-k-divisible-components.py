# 2872. Maximum Number of K-Divisible Components
# Hard


from collections import defaultdict


def maxKDivisibleComponents(
    n: int, edges: list[list[int]], values: list[int], k: int
) -> int:
    # build adj list
    adj = defaultdict(list)

    for v1, v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)

    res = 0

    def dfs(cur, parent):
        total = values[cur]

        for child in adj[cur]:
            if child != parent:
                total += dfs(child, cur)

        if total % k == 0:
            nonlocal res
            res += 1
        return total

    dfs(0, -1)

    return res


print(
    "Example 1: ",
    maxKDivisibleComponents(5, [[0, 2], [1, 2], [1, 3], [2, 4]], [1, 8, 1, 4, 4], 6),
)

# print(
#     "Example 2: ",
#     maxKDivisibleComponents(
#         7, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], [3, 0, 6, 1, 5, 2, 1], 3
#     ),
# )
