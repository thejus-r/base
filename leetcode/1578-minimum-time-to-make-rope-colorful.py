# 1578. Minimum Time to Make Rope Colorful
# Medium

"""
1) untie ballons to make sure there are no consecutive coloured baloons
2) removing ith Balloon takes neededTime[i]

intuition:

When we find a consicutive ballons we find the max(neededTime) for that groups
which will be kept and added to the totalCost(time)

when the group is over, we reset the currentCost to zero?
"""


def minCost(colors: str, neededTime: list[int]) -> int:
    cost, curr_max = 0, 0
    for i in range(len(colors)):
        if i > 0 and colors[i] != colors[i - 1]:
            curr_max = 0
        cost += min(curr_max, neededTime[i])
        curr_max = max(curr_max, neededTime[i])
    return cost


print("Example 1:", minCost("abaac", [1, 2, 3, 4, 5]))
print("Example 2:", minCost("abc", [1, 2, 3]))
print("Example 3:", minCost("aabaa", [1, 2, 3, 4, 1]))
