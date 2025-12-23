def selection_sort(arr: list[int]):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


print("Sorted: ", selection_sort([3, 6, 1, 3, 4, 1]))
