import collections
from typing_extensions import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    q = collections.deque()
    res = []

    q.append(root)
    d = False
    while q:
        qLen = len(q)
        level = []
        for _ in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            if d:
                res.append(level[::-1])
            else:
                res.append(level)
        d = not d
    return res
