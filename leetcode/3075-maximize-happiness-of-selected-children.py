# 3075. Maximize Happiness of Selected Children
# Medium


def maximumHappinessSum(happiness: list[int], k: int) -> int:
    res = 0

    happiness.sort(reverse=True)

    for i in range(k):
        print(res)
        res += happiness[i] - i if happiness[i] - i > 0 else 0

    return res


# print(f"Example 1: {maximumHappinessSum([1, 2, 3], 2)}")
# print(f"Example 2: {maximumHappinessSum([1, 1, 1, 1], 2)}")
# print(f"Example 3: {maximumHappinessSum([2, 3, 4, 5], 1)}")
print(f"Example 4: {maximumHappinessSum([42, 1, 12], 3)}")
