from typing import List
class SparseVector:
    def __init__(self, nums: List[int]) -> None:
        self.lookup = {}

        for index, x in enumerate(nums):
            if x != 0:
                self.lookup[index] = x

    def dotProduct(self, vec: "SparseVector") -> int:
        total = 0

        for key in self.lookup:
            if key in vec.lookup:
                total += self.lookup[key] * vec.lookup[key]
        return total

v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
print("Example 1:", v1.dotProduct(v2))
