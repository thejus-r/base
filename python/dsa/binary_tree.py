from __future__ import annotations

from collections import deque
from typing import Deque


class TreeNode:
    def __init__(
        self, val: int, right: TreeNode | None = None, left: TreeNode | None = None
    ) -> None:
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class BinaryTree:
    def __init__(self, node: TreeNode | None  = None) -> None:
        self.__root: TreeNode | None = node

    def insert(self, data: int):
        newNode = TreeNode(data)

        if self.__root is None:
            self.__root = newNode
            return

        curr = self.__root
        queue: Deque[TreeNode] = deque([curr])

        while queue:
            curr = queue.popleft()

            if curr.left is None:
                curr.left = newNode
                break
            else:
                queue.append(curr.left)

            if curr.right is None:
                curr.right = newNode
                break

            else:
                queue.append(curr.right)

    def in_order(self):
        res = []

        stack = []
        curr = self.__root

        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res

    def level_order(self) -> list[list[int]]:
        if self.__root is None:
            return []

        res: list[list[int]] = []
        q: Deque[TreeNode] = deque([self.__root])
        current_level = 0

        while q:
            len_q = len(q)
            res.append([])

            for _ in range(len_q):
                node = q.popleft()
                res[current_level].append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            current_level += 1

        return res

def build_tree(values: list[int]):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while i < len(values):
        # Get the current parent from the queue
        current = queue.popleft()

        # --- Process Left Child ---
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
            i += 1

        # --- Process Right Child ---
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
            i += 1

    return root


if __name__ == "__main__":
    tree = BinaryTree()

    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)

    print(tree.in_order())
    print(tree.level_order())
