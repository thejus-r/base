# --- Day 7: Laboratories ---

# imports
import time

# file
filename = "./aoc/2025/day-07/input.txt"


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
    lines: list[list[str]] = []
    try:
        with open(filename, "r") as file_object:
            for line in file_object:
                cleanLine = line.rstrip("\n")
                lines.append(list(cleanLine))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


def prettyPrint(gird):
    for r in gird:
        print("".join(r))


@perf_timer
def part1():
    grid = parseInput()

    ROWS, COLS = len(grid), len(grid[0])

    start = grid[0].index("S")

    spliterReached = set()

    def f(r, c):
        if (r, c) in spliterReached:
            return
        # good base case
        if r == ROWS and c <= 0 < COLS:
            return
        # bad base case:
        if r >= ROWS or c < 0 or c >= COLS:
            return

        # when its a beam-spltiter
        if grid[r][c] == "^":
            spliterReached.add((r, c))
            for nc in [c + 1, c - 1]:
                if nc >= 0 and nc < COLS:
                    grid[r][nc] = "|"
                    f(r, nc)

        # when empty
        if grid[r][c] in ".|":
            grid[r][c] = "|"
            f(r + 1, c)

    f(1, start)

    print("Part 1: ", len(spliterReached))


@perf_timer
def part2():
    grid = parseInput()

    ROWS, COLS = len(grid), len(grid[0])

    start = grid[0].index("S")

    def f(r, c, memo={}):
        key = str(r) + "," + str(c)
        if key in memo:
            return memo[key]

        if r == ROWS and 0 <= c < COLS:
            return 1

        if r >= ROWS or c >= COLS or c < 0:
            return 0

        if grid[r][c] in ".|":
            grid[r][c] = "|"
            return f(r + 1, c, memo)

        if grid[r][c] == "^":
            memo[key] = f(r, c + 1, memo) + f(r, c - 1, memo)
            return memo[key]

    res = f(1, start)

    print("Part 2: ", res)


if __name__ == "__main__":
    part1()
    part2()
