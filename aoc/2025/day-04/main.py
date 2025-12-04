filename = "./aoc/2025/day-04/input.txt"


def parseInput():
    lines: list[list[str]] = []
    try:
        with open(filename, "r") as file_object:
            for line in file_object:
                cleanLine = line.strip("\n")
                listOfStr = list(cleanLine)
                lines.append(listOfStr)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


def part1():
    grid = parseInput()

    DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [-1, 1], [1, 1], [-1, -1]]
    ROWS, COLS = len(grid), len(grid[0])

    count = 0

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "@":
                rolls = 0
                for dr, dc in DIRECTIONS:
                    nr = r + dr
                    nc = c + dc

                    if nr >= ROWS or nc >= COLS or nr < 0 or nc < 0:
                        continue

                    if grid[nr][nc] == "@":
                        rolls += 1
                if rolls < 4:
                    count += 1

    print("Part 1: ", count)


def part2():
    grid = parseInput()

    DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [-1, 1], [1, 1], [-1, -1]]
    ROWS, COLS = len(grid), len(grid[0])

    totalCount = 0

    while True:
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "@":
                    rolls = 0
                    for dr, dc in DIRECTIONS:
                        nr = r + dr
                        nc = c + dc

                        if nr >= ROWS or nc >= COLS or nr < 0 or nc < 0:
                            continue

                        if grid[nr][nc] == "@":
                            rolls += 1
                    if rolls < 4:
                        grid[r][c] = "x"
                        count += 1
        print(grid)
        totalCount += count
        if count == 0:
            break

    print("Part 2: ", totalCount)


if __name__ == "__main__":
    # part1()
    part2()
