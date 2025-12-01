# 3069. Distribute Elements Into Two Arrays I
# Easy


def resultArray(nums: list[int]) -> list[int]:
    arr1 = [nums[0]]
    arr2 = [nums[1]]

    for n in nums[2:]:
        if arr1[-1] > arr2[-1]:
            arr1.append(n)
        else:
            arr2.append(n)
    return arr1 + arr2


print("Example 1:", resultArray([2, 1, 3]))
print("Example 2:", resultArray([5, 4, 3, 8]))
