from typing import List
def maxProfit(prices: List[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit

print("Example 1:", maxProfit([7,1,5,3,6,4]))
print("Example 2:", maxProfit([1,2,3,4,5]))