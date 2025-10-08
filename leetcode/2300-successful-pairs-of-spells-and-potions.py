from typing import List
def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:

    # sort portions to do a binary search
    potions.sort()
    res = []

    for spell in spells:
        l, r = 0, len(potions) - 1
        while l <= r:
            m = (r + l) // 2
            if spell * potions[m] < success:
                l = m + 1
            elif spell * potions[m] >= success:
                r = m - 1
        m = (r + l) // 2
        res.append(len(potions) - m - 1)

    return res

# print(f"Example 1: {successfulPairs([5, 1, 3],[1, 2, 3, 4, 5], 7)}")
print(f"Example 2: {successfulPairs([3, 1, 2],[8, 5, 8], 16)}")