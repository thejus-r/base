from collections import defaultdict, deque
from functools import lru_cache
import time


# input files
filename = "./aoc/2025/day-11/input.txt"


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
    lines: list[str] = []
    try:
        with open(filename, "r") as file_object:
            for line in file_object:
                cleanLine = line.rstrip("\n")
                lines.append(cleanLine)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


# -------- PART I --------
def part1():
    inputs = parseInput()

    adj_map = defaultdict(list[str])

    for line in inputs:
        start, connections = line.split(":")
        connection = connections.split()

        for conn in connection:
            adj_map[start].append(conn)

    def bfs():
        res = 0

        visited = set()

        src = "you"
        q = deque()

        visited.add(src)

        q.append(src)

        while q:
            curr = q.popleft()

            if curr == "out":
                res += 1

            for x in adj_map[curr]:
                if x not in visited:
                    visited.add(curr)
                    q.append(x)

        return res

    res = bfs()

    print("Part 1: ", res)


# -------- PART II --------
@perf_timer
def part2():
    inputs = parseInput()

    adj_map = defaultdict(list[str])

    for line in inputs:
        start, connections = line.split(":")
        connection = connections.split()

        for conn in connection:
            adj_map[start].append(conn)

    @lru_cache(maxsize=None)
    def dfs(cur, dac, fft):
        if cur == "out":
            return dac and fft

        else:
            if cur == "dac":
                dac = True
            if cur == "fft":
                fft = True

            return sum([dfs(x, dac, fft) for x in adj_map[cur]])

    res = dfs("svr", False, False)
    print("Part 2: ", res)


if __name__ == "__main__":
    # part1()
    part2()
