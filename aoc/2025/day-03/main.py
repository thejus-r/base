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


def lineAsInts():
    lines = parseInput()
    asInt: list[list[int]] = []
    for line in lines:
        temp: list[int] = []
        for d in line:
            temp.append(int(d))
        asInt.append(temp)

    return asInt


def partOne():
    lines = parseInput()

    ans = 0
    for line in lines:
        m = 0
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                n = int(line[i]) * 10 + int(line[j])
                m = max(m, n)

        ans += m

    print(ans)


def partTwo():
    banks = lineAsInts()

    ans = 0

    for bank in banks:
        remainingSlots = 12
        bankLen = len(bank)

        bankIdx = -1

        batteryEnabled = []
        while remainingSlots > 0:
            maxJolt = max(bank[bankIdx + 1 : bankLen - remainingSlots + 1])
            batteryEnabled.append(maxJolt)

            bankIdx = bank.index(maxJolt, bankIdx + 1)

            remainingSlots -= 1

        jolt = "".join(str(battery) for battery in batteryEnabled)

        ans += int(jolt)

    print(ans)


# partOne()
partTwo()
