# 239 Sliding Window Maximum
# Hard

import unittest
from collections import deque


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []
    q = deque()

    for i, n in enumerate(nums):
        while q and q[-1] < n:
            q.pop()

        q.append(n)

        if i >= k and nums[i - k] == q[0]:
            q.popleft()

        if i >= k - 1:
            res.append(q[0])

    return res


class Test(unittest.TestCase):
    def test(self):

        tests = [
            {
                "nums": [1, 3, -1, -3, 5, 3, 6, 7],
                "k": 3,
                "expected": [3, 3, 5, 5, 6, 7],
            },
            {"nums": [1], "k": 1, "expected": [1]},
        ]
        for t in tests:
            self.assertEqual(maxSlidingWindow(t["nums"], t["k"]), t["expected"])


if __name__ == "__main__":
    unittest.main()
