from typing import Counter


def maxFreqSum(s: str) -> int:
    count = Counter(s)

    vowels = ["a", "e", "i", "o", "u"]

    vFreq, cFreq = 0, 0

    for value, count in count.items():
        if value in vowels:
            vFreq = max(vFreq, count)
        else:
            cFreq = max(cFreq, count)

    return vFreq + cFreq

print("Example 1: ", maxFreqSum("successes"))
print("Example 2: ", maxFreqSum("aeiaeia"))