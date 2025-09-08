from typing import List
def getNoZeroIntegers(n: int) -> List[int]:

    def containsZero(n: int) -> bool:
        numStr = str(n)
        return "0" in numStr

    for i in range(1, n):
        nC = n - i
        if not (containsZero(i) or containsZero(nC)):
            return [i, nC]

    return []
print(getNoZeroIntegers(1010))