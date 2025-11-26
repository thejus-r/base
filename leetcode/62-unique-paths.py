'''
intuition:
    - using dfs to find all possible path
    - or can use dp array, bottom up approach

'''

import unittest


class Solution:
    def uniquePaths(self, m: int, n: int):
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        print(row)

        return row[0]




class TestSolution(unittest.TestCase):

    def setUp(self):
        self.instance = Solution

    # Returns True if the string contains 4 a.
    def test_example_1(self):
        result = self.instance.uniquePaths(self, 3, 7)
        self.assertEqual(result, 28)

if __name__ == '__main__':
    unittest.main()