def fractionToDecimal(numerator: int, denominator: int) -> str:

    negative = False
    if numerator < 0:
        negative = not negative
    if denominator < 0:
        negative = not negative

    def neg(s):
        if negative:
            return f"-{s}"
        return s

    N, D = abs(numerator), abs(denominator)

    whole, reminder = divmod(N , D)

    if reminder == 0:
        return f"{whole}"

    seen = {}
    ans = []
    while reminder > 0:
        reminder *= 10
        digit, reminder = divmod(reminder, D)

        if (digit, reminder) in seen:
            return neg(f"{whole}." + "".join(ans[:seen[(digit, reminder)]]) + "(" + "".join(ans[seen[(digit, reminder)]:]) + ")")

        seen[(digit, reminder)] = len(ans)
        ans.append(str(digit))

    return neg(f"{whole}." + "".join(ans))

# print("Example 1:", fractionToDecimal(1, 2))
# print("Example 1:", fractionToDecimal(3, 7))
# print("Example 1:", fractionToDecimal(3, -1))
# print("Example 1:", fractionToDecimal(1, 3))
print("Example 1:", fractionToDecimal(0, -5))