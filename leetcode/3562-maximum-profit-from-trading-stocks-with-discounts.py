# 3562. Maximum Profit from Trading Stocks with Discounts
# hard


from collections import defaultdict


def maxProfit(
    n: int,
    present: list[int],
    future: list[int],
    hierarchy: list[list[int]],
    budget: int,
) -> int:
    adj = defaultdict(list[int])

    for u, v in hierarchy:
        adj[u - 1].append(v - 1)

    def dfs(u):
        sub_profit = [[0] * (budget + 1) for _ in range(2)]

        for v in adj[u]:
            child_res = dfs(v)
            for state in range(2):
                temp = list(sub_profit[state])

                for b in range(budget, -1, -1):
                    for child_cost in range(budget - b + 1):
                        if b + child_cost <= budget:
                            child_val = child_res[0 if state == 0 else 1][child_cost]
                            temp[b + child_cost] = max(
                                temp[b + child_cost], sub_profit[state][b] + child_val
                            )
                sub_profit[state] = temp

        res = [[0] * (budget + 1) for _ in range(2)]

        p_cost = present[u]
        p_profit = future[u] - present[u]
        p_half_cost = present[u] // 2
        p_half_profit = future[u] - p_half_cost

        for b in range(budget + 1):
            res[0][b] = sub_profit[0][b]

            if b >= p_cost:
                res[0][b] = max(res[0][b], sub_profit[1][b - p_cost] + p_profit)

        for b in range(budget + 1):
            res[1][b] = sub_profit[0][b]

            if b >= p_half_cost:
                res[1][b] = max(
                    res[1][b], sub_profit[1][b - p_half_cost] + p_half_profit
                )

        return res

    return max(dfs(0)[0])


n = 2
present = [1, 2]
future = [4, 3]
hierarchy = [[1, 2]]
budget = 3
print(f"Example 1: {maxProfit(n, present, future, hierarchy, budget)}")
