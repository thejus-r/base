import collections
from typing_extensions import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    depth = 1
    q = collections.deque([root])
    while q:
        qLen = len(q)
        for _ in range(qLen):
            node = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1

    return depth