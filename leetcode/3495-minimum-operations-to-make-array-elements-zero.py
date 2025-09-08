from typing import List
def minOperations(queries: List[List[int]]) -> int:

    res = 0
    for q in queries:
        totalReductions = get(q[1]) - get(q[0] - 1)
        res += (totalReductions + 1) // 2

    return res

def get(num: int) -> int:
    if num == 0:
        return 0
    res = 0
    base = 1
    i = 1
    while True:
        l = 1 << (i - 1) * 2
        r = (1 << i * 2) - 1
        if l > num:
            break
        count = min(r, num) - l + 1
        res += count * base

        base += 1
        i += 1

    return res

print("Example 1:", minOperations([[1,2],[2,4]]))
print("Example 2:", minOperations([[2,6]]))