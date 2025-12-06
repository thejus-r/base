import time

filename = "./aoc/2025/day-05/input.txt"


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
            temp = []
            for line in file_object:
                cleanLine = line.rstrip("\n")
                if cleanLine == "":
                    lines.append(temp)
                    temp = []
                    continue
                temp.append(cleanLine)

            lines.append(temp)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


@perf_timer
def part1():
    good_food_ids, ids = parseInput()

    intervals = []

    for id_range in good_food_ids:
        left, right = id_range.split("-")
        intervals.append([int(left), int(right)])

    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    count = 0
    for id in ids:
        for left, right in merged:
            if left <= int(id) <= right:
                count += 1
                break

    print("Part 1:", count)


@perf_timer
def part2():
    good, id = parseInput()

    arr: list[list[int]] = []

    for rng in good:
        left, right = rng.split("-")
        arr.append([int(left), int(right)])

    arr.sort(key=lambda x: x[0])

    intervals = []

    for ar in arr:
        if not intervals or intervals[-1][1] < ar[0]:
            intervals.append(ar)
        else:
            intervals[-1][1] = max(intervals[-1][1], ar[1])

    ids = 0
    for left, right in intervals:
        ids += (right - left) + 1

    print("Part 2: ", ids)


if __name__ == "__main__":
    part1()
    part2()
