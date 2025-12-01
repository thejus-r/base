from typing import List
from math import ceil


def minEatingSpeed(piles: List[int], h: int) -> int:
    lo, hi = 1, max(piles)
    res = 0

    while lo <= hi:
        speed = (lo + hi) // 2

        total_time_spend = 0
        for pile in piles:
            total_time_spend += ceil(pile / speed)

        if total_time_spend <= h:
            res = speed
            hi = speed - 1
        else:
            lo = speed + 1

    return res


print(f"Example 1: {minEatingSpeed([3, 6, 7, 11], 8)}")  # 4
print(f"Example 2: {minEatingSpeed([30, 11, 23, 4, 20], 5)}")  # 30
print(f"Example 3: {minEatingSpeed([30, 11, 23, 4, 20], 6)}")  # 23

