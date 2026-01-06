# 11. Container With Most Water
# Medium


def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        max_area = max(max_area, (right - left) * min(height[left], height[right]))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_area


input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"Example 1: {maxArea(input)}")

input = [1, 1]
print(f"Example 2: {maxArea(input)}")
