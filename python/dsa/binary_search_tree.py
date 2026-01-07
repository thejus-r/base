from __future__ import annotations


class __TreeNode:
    def __init__(
        self, val: int, right: __TreeNode | None = None, left: __TreeNode | None = None
    ) -> None:
        self.val = val
        self.left: __TreeNode | None = left
        self.right: __TreeNode | None = right


class BST:
    def __init__(self) -> None:
        self.root: __TreeNode | None = None
