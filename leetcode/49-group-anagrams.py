# medium

from typing import List
from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dict = defaultdict(list)

    for s in strs:
        sortedString = "".join(sorted(s))
        dict[sortedString].append(s)

    return [x for x in dict.values()]

print("Example 1: ",groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print("Example 2: ",groupAnagrams([""]))
print("Example 3: ",groupAnagrams(["a"]))
