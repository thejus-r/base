# 199. Binary Tree Right Side View
# Medium

from __future__ import annotations

from collections import deque
from typing import Deque

from dsa.binary_tree import TreeNode


def rightSideView(root: TreeNode | None) -> list[int]:
    res: list[int] = []
    if root is None:
        return res

    queue: Deque[TreeNode] = deque([root])

    while queue:
        queue_width = len(queue)
        level = []

        for _ in range(queue_width):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        res.append(level[-1])

    return res
