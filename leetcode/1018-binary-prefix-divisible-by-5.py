# 1018. Binary Prefix Divisible By 5
# easy


def prefixesDivBy5(nums: list[int]) -> list[bool]:
    ans: list[bool] = []
    prefix = 0

    for num in nums:
        prefix = (prefix << 1) + num % 5
        print(prefix)

        ans.append(prefix == 0)

    print(prefix)
    return ans


print("Example 1", prefixesDivBy5([0, 1, 1]))
print("Example 2", prefixesDivBy5([1, 1, 1]))
