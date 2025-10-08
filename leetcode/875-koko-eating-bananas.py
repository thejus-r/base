from typing import List
from math import ceil
def minEatingSpeed(piles: List[int], h: int) -> int:
    lo, hi = 1, max(piles)
    res = hi

    while lo < hi:
        speed = (hi + lo) // 2
        hrs_taken = 0
        for pile in piles:
            hrs_taken += ceil(pile / speed)
        if hrs_taken <= h:
            res = speed
            hi = speed - 1
        else:
            lo = speed + 1
    return res

print(f"Example 1: {minEatingSpeed([3, 6, 7, 11], 8)}") # 4
print(f"Example 2: {minEatingSpeed([30,11,23,4,20], 5)}") # 30
print(f"Example 3: {minEatingSpeed([30,11,23,4,20], 6)}") # 23