def merge(left: list[int], right: list[int]) -> list[int]:
    result = []

    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def mergeSort(arr: list[int]) -> list[int]:
    n = len(arr)

    if n < 2:
        return arr

    mid = n // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


print("Sorted: ", mergeSort([5, 4, 3, 2, 1, 6]))
print("Sorted: ", mergeSort([5, -1, 3, 3, 1]))
print("Sorted: ", mergeSort([5, 3]))
print("Sorted: ", mergeSort([]))
