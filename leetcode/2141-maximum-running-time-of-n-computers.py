# 2141. Maximum Running Time of N Computers
# Hard


def maxRunTime(n: int, batteries: list[int]) -> int:
    left, right = 1, sum(batteries) // n

    while left < right:
        target = right - (right - left) // 2

        extra = 0

        for power in batteries:
            extra += min(power, target)

        if extra // n >= target:
            left = target
        else:
            right = target - 1

    return left


# print("Example 1:", maxRunTime(2, [3, 3, 3]))
# print("Example 2:", maxRunTime(2, [1, 1, 1, 1]))
print("Example 3:", maxRunTime(3, [10, 10, 3, 5]))  # 8
