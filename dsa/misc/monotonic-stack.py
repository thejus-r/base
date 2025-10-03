from typing import List
def generateMonotonicIncreasingStack(nums: List[int]) -> List[int]:
    stack = []
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack

def generateMonotonicDecreasingStack(nums: List[int]) -> List[int]:
    stack = []
    for num in nums:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    return stack

# Example
nums = [3, 4, 2, 6, 1, 5]
increasing_stack = generateMonotonicIncreasingStack(nums)
decreasing_stack = generateMonotonicDecreasingStack(nums)
print(f"Input: {nums}")
print(f"Monotonic Increasing Stack: {increasing_stack}")
print(f"Monotonic Decreasing Stack: {decreasing_stack}")

# Next Greater Element
def nextGreaterElement(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [-1] * n # Defaults to -1 if no greater element exist

    stack = []
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)

    return stack
