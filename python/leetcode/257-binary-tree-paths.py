# 257. Binary Tree Paths
# Easy

from __future__ import annotations

from dsa.binary_tree import TreeNode


def binaryTreePaths(root: TreeNode | None) -> list[str]:
    res = []

    def paths(node: TreeNode | None, path: list[int] = []):
        if node is None:
            return

        path.append(node.val)

        if not node.left and not node.right:
            res.append("->".join(map(str, path)))

        else:
            paths(node.left)
            paths(node.right)

        path.pop()

    return res
