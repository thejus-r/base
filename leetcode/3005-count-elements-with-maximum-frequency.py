from typing import List
def maxFrequencyElements(nums: List[int]) -> int:

    frequencies = {}
    for num in nums:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1

    max_frequency = 0

    for frequency in frequencies.values():
        max_frequency = max(max_frequency, frequency)

    frequency_of_max_frequency = 0

    for frequency in frequencies.values():
        if frequency == max_frequency:
            frequency_of_max_frequency += 1

    return max_frequency * frequency_of_max_frequency

print("Example 1", maxFrequencyElements([1,2,2,3,1,4])) # 4
print("Example 2", maxFrequencyElements([1,2,3,4,5])) # 5
