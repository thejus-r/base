def findClosest(x: int, y: int, z: int) -> int:
    if abs(z - x) > abs(z - y):
        return 2
    elif abs(z - x) < abs(z - y):
        return 1
    else:
        return 0


print("Example 1: ", findClosest(2, 7, 4))
print("Example 2: ", findClosest(2, 5, 6))
print("Example 3: ", findClosest(1, 5, 3))
