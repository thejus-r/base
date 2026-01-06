from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int, right: TreeNode | None = None, left: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right
