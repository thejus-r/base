from typing import List
from sortedcontainers import SortedList
def avoidFlood(rains: List[int]) -> List[int]:
    ans = [1] * len(rains)
    sunny_days = SortedList()
    full_lakes = {} # lake -> last_rained_day

    for i, rain in enumerate(rains):
        if rain == 0:
            sunny_days.add(i)
            continue
        if rain in full_lakes:
            last_rain_day = full_lakes[rain]
            idx = sunny_days.bisect_right(last_rain_day)

            if idx == len(sunny_days):
                return []
            dry_day = sunny_days[idx]
            ans[dry_day] = rain
            sunny_days.remove(dry_day)

        ans[i] = -1
        full_lakes[rain] = i

    return ans

print(f"Example 1: {avoidFlood([1,2,3,4])}") # [-1,-1,-1,-1]
print(f"Example 2: {avoidFlood([1,2,0,0,2,1])}") # [-1,-1,2,1,-1,-1]
print(f"Example 3: {avoidFlood([1,2,0,1,2])}") # []