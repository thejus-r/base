def intersectionSizeTwo(intervals: list[list[int]]):
    res = 0
    intervals.sort(key=lambda i: (i[1], i[0]))

    p1, p2 = -1, -1

    for left, right in intervals:
        if p2< left:
            res += 2
            p1, p2 = right - 1, right

        elif p1 < left:
            res += 1
            if p2 == right:
                p1 = right - 1
            else:
                p1, p2 = p2, right


    return res

print("Example 1:", intersectionSizeTwo([[1, 3], [3, 7], [8, 9]]))
