# 173. Binary Search Tree Iterator
# Medium

from dsa.binary_tree import TreeNode, build_tree, BinaryTree
import sys

class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.root = root
        self.ptr = -sys.maxsize
        self.stack = []

    def next(self) -> int:
        return 0

    def hasNext(self) -> bool:
        return False


values = [7, 3, 15, None, None, 9, 20]

tree = BinaryTree(build_tree(values))
print(tree.in_order())
