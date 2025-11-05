from collections import defaultdict
from sortedcontainers import SortedList


class XSum:
    def __init__(self, x: int):
        self.x: int = x
        self.result: int = 0
        self.occ: dict[int, int] = defaultdict(int)  # occurance of numbers, default 0
        self.top: SortedList[tuple[int, int]] = SortedList()  # for x top
        self.rest: SortedList[tuple[int, int]] = (
            SortedList()
        )  # stores the rest of the nums

    def insert(self, num: int):
        if self.occ[num] > 0:
            self._internal_remove((self.occ[num], num))
        self.occ[num] += 1
        self._internal_insert((self.occ[num], num))

    def remove(self, num: int):
        self._internal_remove((self.occ[num], num))
        self.occ[num] -= 1
        if self.occ[num] > 0:
            self._internal_insert((self.occ[num], num))

    def get(self):
        return self.result

    def _internal_insert(self, p: tuple[int, int]):
        if len(self.top) < self.x or p > self.top[0]:
            self.result += p[0] * p[1]
            self.top.add(p)
            if len(self.top) > self.x:
                to_remove = self.top[0]
                self.result -= to_remove[0] * to_remove[1]
                self.rest.add(to_remove)
        else:
            self.rest.add(p)

    def _internal_remove(self, p: tuple[int, int]):
        if p >= self.top[0]:
            self.result -= p[0] * p[1]
            self.top.remove(p)
            if self.rest:
                to_add = self.rest[-1]
                self.result += to_add[0] * to_add[1]
                self.rest.remove(to_add)
                self.top.add(to_add)
        else:
            self.rest.add(p)


def findXresult(nums: list[int], k: int, x: int) -> list[int]:
    ans: list[int] = []
    xsum = XSum(x)

    for i in range(len(nums)):
        xsum.insert(nums[i])
        if i >= k:
            xsum.remove(nums[i - k])
        if i >= k - 1:
            ans.append(xsum.get())

    return ans


print("Example 1", findXresult([1, 1, 2, 2, 3, 4, 2, 3], 6, 2))
