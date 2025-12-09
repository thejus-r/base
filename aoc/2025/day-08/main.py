# --- Day 8: Playground ---

# imports
import time
import heapq
import math

# file
filename = "./aoc/2025/day-08/example.txt"


"""
the problem seems like finding connected components, can be solved with unionFind
but, only 3d coordinates are give, so can finding distance between each
pair with the shortest distance gets paied up forming a circut.

example given, for connecting 10 such pair
for part 1, have to do 1000 such connections

result: product of 3 largest circuits
"""


# performance timer decorator
def perf_timer(base_fn):
    def calcTime():
        start_time = time.perf_counter()
        base_fn()
        end_time = time.perf_counter()
        elapsed_time = (end_time - start_time) * 10**6

        print(
            f"Time taken: 🔥{elapsed_time:.2f}μs\n",
        )

    return calcTime


# paser input as lines
def parseInput():
    lines: list[tuple[int, int, int]] = []
    try:
        with open(filename, "r") as file_object:
            for line in file_object:
                cleanLine = line.rstrip("\n")
                s = cleanLine.split(",")
                point = (int(s[0]), int(s[1]), int(s[2]))
                lines.append(point)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


def prettyPrint(gird):
    for r in gird:
        print("".join(r))


def calcDistance(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

        return True


@perf_timer
def part1():
    h = []
    coordinates = parseInput()

    N = len(coordinates)

    for i in range(0, N):
        for j in range(i + 1, N):
            p1 = coordinates[i]
            p2 = coordinates[j]
            d = calcDistance(p1, p2)

            heapq.heappush(h, (d, (i, j)))

    uf = UnionFind(N)

    i = 0

    while i < 10 and h:
        _, pair = heapq.heappop(h)
        uf.union(pair[0], pair[1])
        print(uf.parent)
        i += 1

    print(uf.size)
    sizeArr = []

    for i in range(N):
        sizeArr.append(uf.size[i])

    sizeArr.sort(reverse=True)

    res = math.prod(sizeArr[:3])

    print("Part 1: ", res)


@perf_timer
def part2():
    h = []
    coordinates = parseInput()

    N = len(coordinates)

    for i in range(0, N):
        for j in range(i + 1, N):
            p1 = coordinates[i]
            p2 = coordinates[j]
            d = calcDistance(p1, p2)

            heapq.heappush(h, (d, (i, j)))
    uf = UnionFind(N)

    totalConnections = N

    while h:
        _, pair = heapq.heappop(h)

        if uf.union(pair[0], pair[1]):
            totalConnections -= 1
            if totalConnections == 1:
                print("Part 2: ", coordinates[pair[0]][0] * coordinates[pair[1]][0])
                break


if __name__ == "__main__":
    part1()
    # part2()
