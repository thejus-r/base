class Node:
    def __init__(
        self, value: int, left: Node | None = None, right: Node | None = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def search(self, key: int):
        pass

    def insert(self, key: int):
        if self.root is None:
            self.root = Node(key)

        curr = self.root
        while curr is not None:
            if curr.value > key and curr.left is not None:
                curr = curr.left
            elif curr.value < key and curr.right is not None:
                curr = curr.right
            else:
                break

        if curr.value > key:
            curr.left = Node(key)
        else:
            curr.right = Node(key)

    # get smallest element in the right sub-tree
    def _getSuccessor(self, node: Node) -> Node | None:
        curr = node.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr

    def _deleteNode(self, root: Node | None, key: int) -> Node | None:
        if root is None:
            return root

        if root.value > key:
            root.left = self._deleteNode(root.left, key)
        elif root.value < key:
            root.right = self._deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            succ = self._getSuccessor(root)

            if succ is None:
                raise Exception
            root.value = succ.value
            root.right = self._deleteNode(root.right, succ.value)

        return root

    def delete(self, key: int):
        self.root = self._deleteNode(self.root, key)

    def inOrder(self):
        res = []
        stack = []
        curr = self.root

        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.value)

            curr = curr.right

        return res

    def postOrder(self):
        result = []

        if self.root is None:
            return result

        stack1 = []
        stack2 = []

        stack1.append(self.root)

        while stack1:
            curr = stack1.pop()
            stack2.append(curr)

            if curr.left:
                stack1.append(curr.left)
            if curr.right:
                stack1.append(curr.right)

        while stack2:
            curr = stack2.pop()
            result.append(curr.value)

        return result


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    curr = bst.inOrder()
    print(curr)
    bst.insert(22)
    bst.insert(8)
    bst.insert(4)

    curr = bst.inOrder()
    print(curr)

    bst.delete(10)
    bst.delete(10)
    bst.delete(4)
    bst.delete(8)
    bst.delete(22)
    bst.insert(3)

    curr = bst.inOrder()
    print(curr)
