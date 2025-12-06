import time
import string
from itertools import zip_longest
from math import prod

filename = "./aoc/2025/day-06/input.txt"


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


def parseInput():
    lines = []
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


@perf_timer
def part1():
    lines = parseInput()

    ops = []
    nums = []

    for i, line in enumerate(lines):
        # operators
        if i == len(lines) - 1:
            ops = line.split()
        else:
            nums.append(line.split())

    sumArr = []

    for op in ops:
        if op == "*":
            sumArr.append(1)
        else:
            sumArr.append(0)
    for numArr in nums:
        for i, n in enumerate(numArr):
            if ops[i] == "*":
                sumArr[i] *= int(n)
            else:
                sumArr[i] += int(n)

    print("Part 1:", sum(sumArr))


@perf_timer
def part2():
    lines = parseInput()

    res = 0

    op = None

    chunk = []
    for columns in zip_longest(*lines, fillvalue=" "):
        if op is None or columns[-1] != " ":
            op = columns[-1]

        if all(c in string.whitespace for c in columns):
            if op == "*":
                res += prod(chunk)
            if op == "+":
                res += sum(chunk)

            chunk.clear()
            continue

        number = int("".join(columns[:-1]))
        chunk.append(number)

    if op == "*":
        res += prod(chunk)
    if op == "+":
        res += sum(chunk)

    print("Part 2: ", res)


if __name__ == "__main__":
    part1()
    part2()
