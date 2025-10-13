class Solution:
    def isHappy(self, n: int) -> bool:
        seen: set[int] = set()

        while n not in seen:
            n = self.digitSquareSum(n)

            if n == 1:
                return True
        return False

    def digitSquareSum(self, num: int) -> int:
        sum = 0
        while num:
            digit = num % 10
            sum += digit ** 2
            num = num // 10

        return sum

sol = Solution()
print("Example 1: ", sol.isHappy(19))
