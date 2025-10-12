from functools import cache
from math import comb
def magicalSum(m: int, k: int, nums: list[int]) -> int:
    MOD = 10**9 + 7

    @cache
    def dp(mask: int, m: int, k: int, i: int) -> int:

        # base case
        if m == 0 and mask.bit_count() == k: # successful
            return 1
        if m == 0 or i == len(nums): # un-successful
            return 0

        total = 0
        total += (dp(mask >> 1, m, k - (mask & i), i + 1)) % MOD

        for freq in range(1, m + 1):
            nmask = mask + freq
            next = (dp(mask >> 1, m - freq, k - (nmask & 1), i + 1)) % MOD
            total += (
                pow(nums[i], freq, MOD) * next * comb(m, freq)
            ) % MOD

        return total

    return (dp(0, m, k, 0)) % MOD





print("Example 1: ", magicalSum(5, 5, [1,10,100,10000,1000000]))
print("Example 2: ", magicalSum(2, 2, [5,4,3,2,1]))
