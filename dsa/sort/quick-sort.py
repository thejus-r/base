def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1


def swap(arr: list[int], i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def sort(arr: list[int], low: int, high: int):
    if low < high:
        pi = partition(arr, low, high)

        sort(arr, low, pi - 1)
        sort(arr, pi + 1, high)


def quick_sort(arr: list[int]) -> list[int]:
    sort(arr, 0, len(arr) - 1)
    return arr


print("Sorted: ", quick_sort([5, 4, 2, 5, 3, 1, 4, -1]))
