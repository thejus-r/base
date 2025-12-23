# Simple Union Find
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            x = self.parent[x]
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return False

        self.parent[yRoot] = xRoot
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def reset(self, x: int) -> None:
        self.parent[x] = x
        return
