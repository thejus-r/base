from typing_extensions import Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = 0
        self.left = left
        self.right = right


def isSymmetric(root: Optional[TreeNode]) -> bool:

    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
        if p is None and q is None:
            return True
        if q is None or p is None:
            return False

        if p.val == q.val:
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        return False

    if root is not None:
        return isSameTree(root.left, root.right)
    return False