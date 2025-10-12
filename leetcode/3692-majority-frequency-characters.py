# 3692. Majority Frequency Characters
# Easy

from collections import Counter, defaultdict
def majorityFrequencyGroup(s: str) -> str:
    d: dict[int,list[str]] = defaultdict(list)
    ctr = Counter(s).items()

    for ch, k in ctr:
        d[k].append(ch)

    ans = max(d, key = lambda x: (len(d[x]), x))

    return ''.join(d[ans])


print("Example 1: ", majorityFrequencyGroup("aaabbbccdddde")) # "ab"
print("Example 2: ", majorityFrequencyGroup("abcd")) # "abcd"
print("Example 3: ", majorityFrequencyGroup("pfpfgi")) # "fp"
