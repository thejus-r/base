filename = "input.txt"


def parseInput():
    lines = []
    try:
        with open(filename, "r") as file_object:
            for line in file_object:
                lines.append(line)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


def solution():
    lines = parseInput()

    ans = 0

    cursor = 50
    for line in lines:
        dir = line[0:1]
        val = int(line[1:])

        val *= -1 if dir == "L" else 1

        cursor = (cursor + val) % 100

        if cursor == 0:
            ans += 1

    print(ans)


def part2():
    lines = parseInput()

    count = 0
    cursor = 50

    for line in lines:
        turns, rotation = divmod(int(line[1:]), 100)
        count += turns

        rotation *= 1 if line[0] == "R" else -1

        if line[0] == "R":
            if cursor + rotation >= 100:
                count += 1
        else:
            if cursor > 0 and (cursor + rotation) <= 0:
                count += 1

        cursor = (cursor + rotation) % 100

    print(count)


# solution()
part2()
