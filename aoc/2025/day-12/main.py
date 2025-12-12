from collections import defaultdict
import enum
import time


# input files
filename = "./aoc/2025/day-12/input.txt"


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
    input_groups: list = []
    lines: list = []
    try:
        with open(filename, "r") as file_object:
            for line in file_object:
                if line == "\n":
                    input_groups.append(lines)
                    lines = []
                    continue
                lines.append(line.rstrip("\n"))

            input_groups.append(lines)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return input_groups


# -------- PART I --------
def part1():
    input_groups = parseInput()

    section1 = input_groups[:-1]
    section2 = input_groups[-1]

    # calculate area
    print(section1)

    shape_area_map = defaultdict(int)

    for i, shape in enumerate(section1):
        for row in shape[1:]:
            shape_area_map[i] += row.count("#")

    print(shape_area_map)

    count = 0

    for inputLine in section2:
        dim, qty = inputLine.split(":")
        r, c = map(int, dim.split("x"))
        m = r * c

        req = 0
        for i, q in enumerate(qty.split()):
            req += int(q) * shape_area_map[i]

        space_left = m - req

        if space_left > 200:
            print(
                f"{'\033[0;32m'}[Safe Packing ]{'\033[0m'} Available Space: {m}, Required Space: {req}, Diff: {space_left}"
            )
            count += 1
        elif 0 <= space_left < 200:
            print(
                f"{'\033[0;31m'}[Close Packing]{'\033[0m'} Available Space: {m}, Required Space: {req}, Diff: {space_left}"
            )
        else:
            print(
                f"[No Space     ] Available Space: {m}, Required Space: {req}, Diff: {space_left}"
            )

    print("Part 1: ", count)


if __name__ == "__main__":
    part1()
