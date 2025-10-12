def sumOddLengthSubarrays(arr: list[int]) -> int:
    N = len(arr)

    total = 0
    for k in range(1, N + 1, 2):
        for t in range(N - k + 1):
            total += sum(arr[t:t+k])



    return total

print("Example 1:", sumOddLengthSubarrays([1,4,2,5,3]))
print("Example 2:", sumOddLengthSubarrays([1,2]))
