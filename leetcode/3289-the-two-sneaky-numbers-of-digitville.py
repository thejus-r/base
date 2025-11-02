# 3289. The Two Sneaky Numbers of Digitville
# Easy

# Approach 1: Hash Set
def approach1(nums: list[int]) -> list[int]:
    seen: set[int] = set()
    res: list[int] = []

    for num in nums:
        if num in seen:
            res.append(num)
        if len(res) == 2:
            break
        seen.add(num)

    return res


# Approach 2: Bitwise Operations
def approach2(nums: list[int]) -> list[int]:
    n = len(nums) - 2
    y = 0
    for x in nums:
        y ^= x
    for i in range(n):
        y ^= i
    lowBit = y & -y
    x1 = x2 = 0
    for x in nums:
        if x & lowBit:
            x1 ^= x
        else:
            x2 ^= x
    for i in range(n):
        if i & lowBit:
            x1 ^= i
        else:
            x2 ^= i
    return [x1, x2]


print("approach2", approach2([0, 1, 2, 3, 3, 4, 4]))
