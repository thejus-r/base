def makeTheIntergerZero(num1: int, num2: int) -> int:

    k = 1
    while True:
        x = num1 - k * num2

        if x < k:
            return -1
        if x.bit_count() <= k:
            return k

        k += 1

print("Example 1: ", makeTheIntergerZero(3, -2))
print("Example 2: ", makeTheIntergerZero(5, 7))
