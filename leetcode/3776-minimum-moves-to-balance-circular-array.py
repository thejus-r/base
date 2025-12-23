# 3776. Minimum Moves to Balance Circular Array
# Medium

"""
Intuition:
    1 - the list has atmost one negative values, so we have to check it the list needs to be
        balanced

    2 - we check if its possible to balance, if the sum of rest is greater than the
        negative value

    We can sort the values by index
"""


def minMoves(balance: list[int]) -> int:
    negIdx = 0
    n = len(balance)

    if sum(balance) < 0:
        return -1

    for i, val in enumerate(balance):
        if val < 0:
            negIdx = i

    if negIdx == -1:
        return 0

    arr = []
    for i, val in enumerate(balance):
        if i != negIdx:
            dist = min((i - negIdx) % n, (negIdx - i) % n)
            arr.append((dist, val))

    b = -balance[negIdx]

    arr.sort()

    print(arr)
    moves = 0
    for dist, val in arr:
        moves += min(val, b) * dist
        print(moves)
        b -= val

        if b <= 0:
            break

    return moves


print(f"Example 1: {minMoves([5, 1, -4])}")
print(f"Example 2: {minMoves([1, 2, -5, 2])}")
print(f"Example 3: {minMoves([7, 5, -1])}")
