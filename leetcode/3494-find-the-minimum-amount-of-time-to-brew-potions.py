# MUST REVIST
def minTime(skill: list[int], mana: list[int]) -> int:
    n, m = len(skill), len(mana)

    # Prefix Sum
    prefix_skill = [0] * n
    for i in range(1, n):
        prefix_skill[i] = prefix_skill[i - 1] + skill[i]

    total_time = skill[0] * mana[0]
    for j in range(1, m):
        max_time = skill[0] * mana[j]
        for i in range(1, n):
            diff_time = mana[j - 1] * prefix_skill[i] - mana[j] * prefix_skill[i - 1]
            if diff_time > max_time:
                max_time = diff_time
        total_time += max_time
    return total_time + mana[-1] * prefix_skill[-1]


print(f"Example 1: {minTime([1, 5, 2, 4], [5, 1, 4, 2])}")  # 110
print(f"Example 2: {minTime([1, 1, 1], [1, 1, 1])}")  # 5
print(f"Example 3: {minTime([1, 2, 3, 4], [1, 2])}")  # 21
print(f"Example 4: {minTime([3, 5, 3, 9], [1, 10, 7, 3])}")  # 293
