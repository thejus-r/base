from typing import List
from math import gcd, lcm
def replaceNonCoprimes(nums: List[int]) -> List[int]:
    stack = []

    for x in nums:
        stack.append(x)

        while len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
            a = stack.pop()
            b = stack.pop()

            l = lcm(a, b)
            stack.append(l)

    return stack

print("Example 1:", replaceNonCoprimes([6,4,3,2,7,6,2]))
print("Example 2:", replaceNonCoprimes([2,2,1,1,3,3,3]))