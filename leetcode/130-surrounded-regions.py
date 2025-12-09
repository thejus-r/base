# 130. Surrounded Regions
# Medium


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            parent = self.parent[self.parent[x]]
            return self.find(parent)
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False

        self.parent[y_root] = x_root

        return True


def solve(board: list[list[str]]) -> None:
    uf = UnionFind(10)
    print(uf.parent)

    uf.union(1, 2)

    print(uf.parent)
    print(uf.parent)
    print(board)


solve([])
