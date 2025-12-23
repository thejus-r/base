from collections import defaultdict


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        xRep = self.find(x)
        yRep = self.find(y)

        # We return false, as its already connected
        if xRep == yRep:
            return False

        if self.rank[xRep] > self.rank[yRep]:
            self.parent[yRep] = xRep
        elif self.rank[xRep] < self.rank[yRep]:
            self.parent[xRep] = yRep
        else:
            self.parent[yRep] = xRep
            self.rank[xRep] += 1

        return True

    def reset(self, x: int) -> None:
        self.parent[x] = x
        self.rank[x] = 0


def findAllPeople(n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
    meetings.sort(key=lambda x: x[2])
    meetingsByTime = defaultdict(list)

    uf = UnionFind(n)
    uf.union(firstPerson, 0)

    for p1, p2, t in meetings:
        meetingsByTime[t].append((p1, p2))

    for t in meetingsByTime:
        for p1, p2 in meetingsByTime[t]:
            uf.union(p1, p2)

        for p1, p2 in meetingsByTime[t]:
            if not uf.connected(p1, 0):
                uf.reset(p1)
                uf.reset(p2)

    print(list(range(n)))
    print(uf.parent)
    return [i for i in range(n) if uf.connected(i, 0)]


print(f"Example 1: {findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1)}")
