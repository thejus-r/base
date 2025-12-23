# 2054. Two Best Non-Overlapping Events
# Medium

import math


def maxTwoEvents(events: list[list[int]]) -> int:
    events.sort(key=lambda x: (x[0], x[1]))
    suffixMax = [0] * len(events)
    suffixMax[-1] = events[-1][2]

    for i in reversed(range(len(suffixMax) - 1)):
        suffixMax[i] = max(events[i][2], suffixMax[i + 1])

    result = 0

    for i in range(len(events)):
        nextNotIntersectedEventIndex = binary(events, events[i][1])

        if nextNotIntersectedEventIndex != -1:
            result = max(result, events[i][2] + suffixMax[nextNotIntersectedEventIndex])

        result = max(result, suffixMax[i])

    print(events)
    print(suffixMax)

    return result


def binary(events, time):
    left = 0
    right = len(events) - 1

    while right - left > 1:
        mid = math.ceil((right - left) / 2) + left

        if events[mid][0] <= time:
            left = mid
        else:
            right = mid

    if time >= events[right][0]:
        return -1

    return right


print(f"Example 1: {maxTwoEvents([[1, 3, 2], [4, 5, 2], [2, 4, 3]])}")
