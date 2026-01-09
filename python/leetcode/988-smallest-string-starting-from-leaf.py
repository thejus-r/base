# 988. Smallest String Starting From Leaf
# Medium

from dsa.binary_tree import TreeNode

class Solution:
    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        self.smallestString = ""
        self.smallestString = self.findSmallest(root, "")
        return ""

    def findSmallest(self, node: TreeNode | None, current_string: str):
        if not node:
            return

        current_string = chr(node.val + ord('a')) + current_string

        # not a leaf node
        if not node.left and not node.right:
            if not self.smallestString or current_string < self.smallestString:
                self.smallestString = current_string

        if node.left:
            self.findSmallest(node.left, current_string)

        if node.right:
            self.findSmallest(node.right, current_string)
