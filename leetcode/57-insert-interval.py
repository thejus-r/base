def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    i = 0
    n = len(intervals)
    res: list[list[int]] = []


    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    while i < n and newInterval[1] >= intervals[i][0]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    res.append(newInterval)

    while i < n:
        res.append(intervals[i])
        i += 1
    return res

print("Example 1:", insert([[1, 3], [6, 9]], [2, 5])) # [[1,5],[6,9]]
