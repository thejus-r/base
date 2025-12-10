import time
from collections import defaultdict

import z3

# input files
filename = "./aoc/2025/day-10/input.txt"


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
    lines: list[tuple[str, list[list[int]], list[int]]] = []
    try:
        with open(filename, "r") as file_object:
            for line in file_object:
                cleanLine = line.rstrip("\n")
                split = cleanLine.split(" ")

                config = split[0][1:-1]
                buttonList = []

                for buttons in split[1:-1]:
                    clean = [int(button) for button in buttons[1:-1].split(",")]
                    buttonList.append(clean)

                joltages = [int(jolt) for jolt in split[-1][1:-1].split(",")]
                lines.append((config, buttonList, joltages))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


# ---- PART 1 ----
@perf_timer
def part1():
    inputs = parseInput()

    def f(
        curr: str, target: str, i: int, buttonsPressed: list[int], seen=defaultdict(int)
    ):
        # good base case
        if curr == target:
            return combos.append(len(buttonsPressed))

        if i >= len(buttons):
            return []

        # bad base case, we have already seen this before
        # already reached we are doing unwanted work
        if curr in seen and seen[curr] > 1:
            return []

        nextList = list(curr)
        buttonsPressed.append(i)
        for b in buttons[i]:
            nextList[b] = "#" if nextList[b] == "." else "."

        next = "".join(nextList)
        seen[next] += 1
        f(next, target, i + 1, buttonsPressed, seen)

        seen[next] -= 1
        buttonsPressed.pop()
        f(curr, target, i + 1, buttonsPressed, seen)

    ans = 0
    for config, buttons, _ in inputs:
        startString = "".join(["." * len(config)])
        combos = []
        f(startString, config, 0, [])
        ans += min(combos)

    print("Part 1: ", ans)


# ---- PART 2 ----
@perf_timer
def part2():
    inputs = parseInput()

    ans = 0
    for _, buttonsCombos, jolts in inputs:
        presses = [z3.Int(f"press{i}") for i in range(len(buttonsCombos))]

        s = z3.Optimize()
        s.add(z3.And([press >= 0 for press in presses]))

        s.add(
            z3.And(
                [
                    sum(
                        presses[j]
                        for j, button in enumerate(buttonsCombos)
                        if i in button
                    )
                    == jolt
                    for i, jolt in enumerate(jolts)
                ]
            )
        )

        s.minimize(sum(presses))

        assert s.check() == z3.sat

        m = s.model()
        for press in presses:
            ans += m[press].as_long()

    print("Part 2: ", ans)


# ---- DRIVER CODE ----
if __name__ == "__main__":
    part1()
    part2()
