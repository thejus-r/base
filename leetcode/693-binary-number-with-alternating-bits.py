def hasAlternatingBits(n: int) -> bool:

    temp = bin(n)[2:]

    for i in range(1, len(temp)):
        if (temp[i] == temp[i - 1]):
            return False

    return True

print("Example 1: ", hasAlternatingBits(13))