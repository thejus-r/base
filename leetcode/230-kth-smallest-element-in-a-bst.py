from heapq import heapify, heappop, heappush
import re


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def kthSmallest(root: TreeNode | None, k: int) -> int:
    def inorder(node):
        if node is None:
            return []

        return inorder(node.left) + [node.val] + inorder(node.right)

    sortedElements = inorder(root)
    return sortedElements[k - 1]


root = TreeNode(3, TreeNode(1, None), TreeNode(4, None))

print("Example 1: ", kthSmallest(root, 2))
