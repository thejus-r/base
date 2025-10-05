import collections
from typing_extensions import Optional
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:

    res = []
    q = collections.deque()
    q.append(root)

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
            res.append(level)

    return res