# 756. Pyramid Transition Matrix
# Medium


import collections


def pyramidTransition(bottom: str, allowed: list[str]) -> bool:
    # we first create a lookup table, for easier access
    T = collections.defaultdict(set)

    for u, v, w in allowed:
        T[u, v].add(w)

    def solve(A):
        if len(A) == 1:
            return True
        return any(solve(cand) for cand in backtrack(A, []))

    # we can try all combination and back track is that combination is not possible
    def backtrack(A, ans, i=0):
        # base case
        if i + 1 == len(A):
            yield "".join(ans)
        else:
            for w in T[A[i], A[i + 1]]:
                ans.append(w)
                for result in backtrack(A, ans, i + 1):
                    yield result

                ans.pop()

    bottom_list = list(bottom)

    return solve(bottom_list)


print(f"Example 1: {pyramidTransition('BCD', ['BCC', 'CDE', 'CEA', 'FFF'])}")
print(f"Example 2: {pyramidTransition('AAAA', ['AAB', 'AAC', 'BCD', 'BBE', 'DEF'])}")
