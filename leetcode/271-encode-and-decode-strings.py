# medium

from typing import List

def encode(strs: List[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(str) -> List[str]:
    res, i = [], 0

    while i < len(str):
        j  = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j + 1: j + 1 + length])
        i = j + 1 + length

    return res


encoded = encode(["neet","code","love","you"])
print(encoded)
decoded = decode(encoded)
print(decoded)
