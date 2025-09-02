# Leetcode: 43
# Multiply Strings
# https://leetcode.com/problems/multiply-strings
# medium

class Solution:
    def multiply(self, num1: str, num2: str):

        if "0" in [num1, num2]:
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]

        res = [0]* (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] +=  int(num1[i]) * int(num2[j])
                res[i+j + 1] +=  res[i+j] // 10
                res[i+j] =  res[i+j] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)


sol = Solution()
print("Example 1:", sol.multiply("2", "3"))
print("Example 2:", sol.multiply("123", "456"))
print("Example 3:", sol.multiply("0", "456"))
print("Example 3:", sol.multiply("1292903509936727404199686220192411623085", "9996190433341303536650999221082973702747291324607482481306424831201698419742124862320482024"))
