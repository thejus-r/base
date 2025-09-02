from typing import List
from collections import Counter

# with inbuild Counter with nLargest of MaxHeap
def topKFrequent(nums: List[int], k: int) -> List[int]:
    res = Counter(nums)
    kTop = res.most_common(k)
    top = []

    for key, _ in kTop:
        top.append(key)

    return top

# bucket-sort
def topKFrequentBucketSort(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for _ in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

    return res

print("Example 1:", topKFrequent( [1,1,1,2,2,3], 2))
print("Example 2:", topKFrequent([1], 1))
print("Example 3:", topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))
print("Example 4:", topKFrequent([5,5,5,7,7,9,8,8,8,8], 2))
