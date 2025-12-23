# 955. Delete Columns to Make Sorted II
# Medium

"""
Intuition:
    we try to add the columns, instead of trying to delete them
"""


def minDeletionSize(strs: list[str]) -> int:
    def is_sorted(strs):
        return all([strs[i] <= strs[i + 1] for i in range(len(strs) - 1)])

    deletions = 0
    curr = [""] * len(strs)

    for col in zip(*strs):
        currNext = curr[:]

        for i, letter in enumerate(col):
            currNext[i] += letter

        if is_sorted(currNext):
            curr = currNext
        else:
            deletions += 1

    return deletions


print(f"Example 1: {minDeletionSize(['ca', 'bb', 'ac'])}")  # 1
print(f"Example 2: {minDeletionSize(['xc', 'yb', 'za'])}")  # 0
print(f"Example 3: {minDeletionSize(['zyx', 'wvu', 'tsr'])}")  # 3
