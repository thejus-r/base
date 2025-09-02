# Leetcode: 3021
# Alice and Bob Playing Flower Game
# https://leetcode.com/problems/alice-and-bob-playing-flower-game
# medium

# Dry Run from Smallest case, you will figure it out! Why this answer
def flowerGame(n: int, m: int) -> int:
    oddN, evenN = (n + 1) // 2, n // 2
    oddM, evenM = (m + 1) // 2, m // 2

    return evenM * oddN + oddM * evenN


print("Example 1: ", flowerGame(3,2))
print("Example 2: ", flowerGame(1,1))
