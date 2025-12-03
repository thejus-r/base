# 3625. Count Number of Trapezoids II
# Hard

"""
Intuition:
    - group points by slop
    - slop: (y2 - y1) / (x2 - x1)
    - find edges by no of points present in each group
"""

from collections import Counter, defaultdict
from fractions import Fraction


def countTrapezoids(points: list[list[int]]) -> int:
    n = len(points)
    inf = 10**9 + 7

    slope_to_intercept = defaultdict(list)
    mid_to_slope = defaultdict(list)

    ans = 0

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            dx, dy = x2 - x1, y2 - y1

            if dx != 0:
                s = Fraction(dy / dx)
                b = y1 - (s * x1)  # y-axis interscept

            else:
                s = inf
                b = x1

            slope_to_intercept[s].append(b)
            mid = (x1 + x2, y1 + y2)

            mid_to_slope[mid].append(s)

            for intersepts_in_same_slop in slope_to_intercept.values():
                if len(intersepts_in_same_slop) == 1:
                    continue
                c = Counter(intersepts_in_same_slop)

                acc = 0
                for count in c.values():
                    ans += acc * count
                    acc += count

            for slopes_in_same_mid in mid_to_slope.values():
                if len(slopes_in_same_mid) == 1:
                    continue
                c = Counter(slopes_in_same_mid)

                acc = 0
                for count in c.values():
                    ans -= acc * count
                    acc += count

    return ans


print("Example 1:", countTrapezoids([[-3, 2], [3, 0], [2, 3], [3, 2], [2, -3]]))
