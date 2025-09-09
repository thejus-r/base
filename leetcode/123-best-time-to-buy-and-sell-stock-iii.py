from typing import List
def maxProfit(prices: List[int]) -> int:
    t1, t2 = float("inf"), float("inf")
    p1, p2 = 0,0

    for p in prices:
        t1 = min(t1, p)
        p1 = max(p1, p - t1)

        t2 = min(t2, p - p1)
        p2 = max(p2, p - t2)

    return int(p2)

print("Example 1: ", maxProfit([1,2,3,4,5]))