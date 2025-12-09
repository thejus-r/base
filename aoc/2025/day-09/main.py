from itertools import combinations
import time


# input files
filename = "./aoc/2025/day-09/input.txt"

"""
    ..............
    .......#...#..
    ..............
    ..#....#......
    ..............
    ..#......#....
    ..............
    .........#.#..
    ..............

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
    lines: list[list[int]] = []
    try:
        with open(filename, "r") as file_object:
            for line in file_object:
                cleanLine = line.rstrip("\n")
                s = cleanLine.split(",")
                point = [int(s[0]), int(s[1])]
                lines.append(point)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


# ---- PART 1 ----
@perf_timer
def part1():
    redTiles = parseInput()

    redTiles.sort()

    maxArea = 0

    for i in range(len(redTiles)):
        for j in range(i + 1, len(redTiles)):
            p1 = redTiles[i]
            p2 = redTiles[j]

            area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)

            maxArea = max(area, maxArea)

    print("Part 1: ", maxArea)


# ---- PART 2 ----
@perf_timer
def part2():
    corners = parseInput()
    num_corners = len(corners)

    vertical_edges = []
    horizontal_edges = []

    for i in range(num_corners):
        p1 = corners[i]
        p2 = corners[(i + 1) % num_corners]

        if p1[0] == p2[0]:  # vertical line
            y_min, y_max = sorted([p1[1], p2[1]])
            vertical_edges.append((p1[0], y_min, y_max))
        else:
            x_min, x_max = sorted([p1[0], p2[0]])
            horizontal_edges.append((x_min, x_max, p1[1]))

    def is_point_inside(px: float, py: float) -> bool:
        intersections = 0
        for vx, vy_min, vy_max in vertical_edges:
            if vx > px:
                if vy_min <= py < vy_max:
                    intersections += 1
        return intersections % 2 == 1

    def intersects_rect(r_min_x, r_min_y, r_max_x, r_max_y) -> bool:
        for vx, vy_min, vy_max in vertical_edges:
            if r_min_x < vx < r_max_x:
                overlap_min = max(vy_min, r_min_y)
                overlap_max = min(vy_max, r_max_y)

                if overlap_min < overlap_max:
                    return True

        for hx_min, hx_max, hy in horizontal_edges:
            if r_min_y < hy < r_max_y:
                overlap_min = max(hx_min, r_min_x)
                overlap_max = min(hx_max, r_max_x)

                if overlap_min < overlap_max:
                    return True

        return False

    max_area = 0

    for p1, p2 in combinations(corners, 2):
        width = abs(p1[0] - p2[0]) + 1
        height = abs(p1[1] - p2[1]) + 1
        area = width * height

        if area <= max_area:
            continue

        r_min_x, r_max_x = sorted([p1[0], p2[0]])
        r_min_y, r_max_y = sorted([p1[1], p2[1]])

        if is_point_inside(r_min_x + 0.5, r_min_y + 0.5):
            if not intersects_rect(r_min_x, r_min_y, r_max_x, r_max_y):
                max_area = area

    print("Part 2: ", max_area)


# ---- DRIVER CODE ----
if __name__ == "__main__":
    part1()
    part2()
