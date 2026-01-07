# 515. Find Largest Value in Each Tree Row
# Medium

from __future__ import annotations

import sys
from collections import deque
from typing import Deque

from dsa.binary_tree import TreeNode


def largestValues(root: TreeNode | None) -> list[int]:
    res = []

    if root is None:
        return res

    queue: Deque[TreeNode] = deque([root])

    while queue:
        level_width = len(queue)
        max_val = -sys.maxsize

        for _ in range(level_width):
            node = queue.popleft()

            if node.val > max_val:
                max_val = node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        res.append(max_val)

    return res
