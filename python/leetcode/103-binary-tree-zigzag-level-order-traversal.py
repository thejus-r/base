# 103. Binary Tree Zigzag Level Order Traversal
# Medium

from __future__ import annotations

from collections import deque
from typing import Deque

from dsa.binary_tree import TreeNode


def zigzagLevelOrder(root: TreeNode | None) -> list[list[int]]:
    res: list[list[int]] = []

    if root is None:
        return res

    queue: Deque[TreeNode] = deque([root])
    curr_level = 0

    while queue:
        level_width = len(queue)
        level: list[int] = []

        for _ in range(level_width):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if curr_level % 2 == 0:
            res.append(level)
        else:
            res.append(level[::-1])

    return res
