def numWaterBottles(numBottles: int, numExchange: int) -> int:
    count = 0

    while numBottles >= numExchange:
        count += numExchange
        numBottles -= numExchange

        numBottles += 1

    return count + numBottles

print(f"Example 1: {numWaterBottles(9, 3)}")
print(f"Example 2: {numWaterBottles(15, 4)}")