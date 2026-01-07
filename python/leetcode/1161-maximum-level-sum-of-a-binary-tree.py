from dsa.binary_tree import TreeNode


def maxLevelSum(root: TreeNode | None) -> int:
    if root is None:
        return 0

    q = []
    res = []

    q.append(root)
    curr_level = 0

    while q:
        len_q = len(q)
        res.append([])

        for _ in range(len_q):
            node = q.pop(0)

            res[curr_level].append(node.val)

            if node.left is not None:
                q.append(node.left)

            if node.right is not None:
                q.append(node.right)

        curr_level += 1

    max_sum = root.val
    maximal_sum_level = 1

    for lvl, row in enumerate(res):
        level_sum = sum(row)
        if level_sum > max_sum:
            max_sum = level_sum
            maximal_sum_level = lvl + 1

    return maximal_sum_level
