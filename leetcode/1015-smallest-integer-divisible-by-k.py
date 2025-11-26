def smallestRepunitDivByK(k: int) -> int:
    prefix = 0
    preSet = set()
    n = 0
    while True:
        n += 1
        prefix = (prefix * 10 + 1) % k
        if prefix == 0:
            return n

        if prefix in preSet:
            return -1
        else:
            preSet.add(prefix)


print("Example 1: ", smallestRepunitDivByK(1))  # 1 1 div by 1
print("Example 2: ", smallestRepunitDivByK(2))  # -1, nil
print("Example 3: ", smallestRepunitDivByK(3))  # 3 , 111 div by 3
