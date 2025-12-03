# Change input filename to example / input
filename = "input.txt"


def parseInput():
    lines = []
    try:
        with open(filename, "r") as file_object:
            for line in file_object:
                lines.append(line.rstrip("\n"))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


def partOne():
    def f(start: int, end: int) -> int:
        count = 0
        for n in range(start, end + 1):
            nStr = str(n)
            mid = len(nStr) // 2

            if nStr[mid:] == nStr[:mid]:
                count += n

        return count

    res = 0

    input = parseInput()[0]
    ranges = input.split(",")
    for r in ranges:
        bounds = r.split("-")
        res += f(int(bounds[0]), int(bounds[1]))

    print("Part 1: ", res)


def partTwo():
    def f(start: int, end: int) -> int:
        s = 0

        for n in range(start, end + 1):
            nStr = str(n)
            if nStr in (nStr + nStr)[1:-1]:
                s += n
        return s

    res = 0

    input = parseInput()[0]
    ranges = input.split(",")
    for r in ranges:
        bounds = r.split("-")
        res += f(int(bounds[0]), int(bounds[1]))

    print("Part 2: ", res)


partOne()
partTwo()
