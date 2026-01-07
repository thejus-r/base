# 1339. Maximum Product of Splitted Binary Tree
# Medium

from collections import deque
from typing import Deque

from dsa.binary_tree import TreeNode


def maxProduct(root: TreeNode | None) -> int:
    # find sum at reach nodes

    if root is None:
        return 0

    def sumTree(node: TreeNode | None) -> int:
        if not node:
            return 0

        node.val += sumTree(node.left) + sumTree(node.right)
        return node.val

    total = sumTree(root)

    # maximize sum of sumTree * (total - sum of subTree)
    # process all node to compare

    queue: Deque[TreeNode] = deque([root])

    max_product = 0

    while queue:
        node = queue.popleft()

        curr_product = (total - node.val) * node.val
        max_product = max(curr_product, max_product)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return max_product
