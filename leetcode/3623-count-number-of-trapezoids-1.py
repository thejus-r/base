# 3623. Count Number of Trapezoids I
# Medium

from collections import defaultdict


def countTrapezoids(points: list[list[int]]) -> int:
    mod = 10**9 + 7
    groups = defaultdict(int)

    ans = 0
    total_sum = 0

    for _, y in points:
        groups[y] += 1

    for p in groups.values():
        edges = (p * (p - 1)) // 2

        print(edges)

        ans = (ans + edges * total_sum) % mod
        total_sum = (total_sum + edges) % mod

    return ans


print(
    "Example 1: ",
    countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]),
)
