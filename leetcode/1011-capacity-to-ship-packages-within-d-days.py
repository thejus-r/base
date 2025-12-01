# 1011. Capacity To Ship Packages Within D Days
# Medium


def shipWithinDays(weights: list[int], days: int) -> int:
    # find total weight and max weight
    totalWeight, maxWeight = 0, -1

    for weight in weights:
        totalWeight += weight
        maxWeight = max(maxWeight, weight)

    lo, hi = maxWeight, totalWeight
    optimalShipLimit = maxWeight

    # binary search to find the optimal ship weight limit
    while lo <= hi:
        shipLimit = (lo + hi) // 2

        currentWeight, numberOfDays = 0, 0

        for weight in weights:
            if currentWeight + weight > shipLimit:
                numberOfDays += 1
                currentWeight = 0
            currentWeight += weight

        if numberOfDays < days:
            optimalShipLimit = shipLimit
            hi = shipLimit - 1
        else:
            lo = shipLimit + 1

    return optimalShipLimit


print("Example 1: ", shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print("Example 2: ", shipWithinDays([3, 2, 2, 4, 1, 4], 3))
