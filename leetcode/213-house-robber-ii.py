# 213. House Robber II
# Medium

'''
    Inituition:
        - Similar to House Robber I
        - to solve for the cycle, which gives use only two case since House[1] and House[n] are adjacent:
            1. we take 1 <-> n - 1
            2. we take 2 <-> n

            the take the max of the 2, that would be the result

        pseudo code

        function 
'''
def rob(nums: list[int]) -> int:

    def f(i, memo: dict):
        pass




    return 0

print("Example 1: ", [2, 3, 2]) # 3
# print("Example 2: ", [1, 2, 3, 1]) # 4
# print("Example 3: ", [1, 2, 3]) # 3