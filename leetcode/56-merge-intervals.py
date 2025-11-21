def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda i: i[0])

    merged: list[list[int]] = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


print(
    "Example 1:", merge([[1, 3], [2, 6], [8, 10], [15, 18]])
)  # [[1,6],[8,10],[15,18]]
