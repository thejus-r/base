def rob(nums: list[int]) -> int:
    n = len(nums)

    def f(i, memo: dict):
        if i == n:
            return 0
        if i == n - 1:
            return nums[n - 1]
        
        if i not in memo:
            rob = nums[i] + f(i + 2, memo)
            skip = f(i + 1, memo)

            memo[i] = max(rob, skip)

        return memo[i]
        
    return f(0, {})

 

print("Example 1: ", rob([6, 1, 1, 7]))