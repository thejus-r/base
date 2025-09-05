from typing import List
def read_2d_number_matrix(filename: str) -> List[List[int]]:
    matrix: List[List[int]] = []
    try:
        with open(filename) as file:
            for line in file:
                 row_str = line.strip().split()
                 row_int = list(map(int, row_str))
                 matrix.append(row_int)
    except FileNotFoundError:
        print("Error: File not found")
    except ValueError:
        print("Error: Invalid data in file. Ensure all elements are numbers.")

    return matrix

def main():
    data = read_2d_number_matrix("input.txt")

    def checkDirection(prev, curr) -> int:
        if prev > curr:
            return 1
        elif prev < curr:
            return -1
        return 0

    def check_if_safe(report: List[int]) -> bool:
        levelDirection = 0
        safe = True
        for y in range(1, len(report)):
            if levelDirection == 0:
                levelDirection = checkDirection(report[y], report[y - 1])
                if levelDirection == 0:
                    safe = False
            if levelDirection != checkDirection(report[y], report[y - 1]) or not (1 <= abs(report[y] - report[y - 1]) <= 3):
                safe = False

        return safe

    def try_damping(report: List[int]) -> bool:
        for i in range(0, len(report)):
            modifyReport = report.copy()
            del modifyReport[i]
            if check_if_safe(modifyReport):
                return True
        return False

    safeCount = 0
    for x in data:
        if check_if_safe(x):
            safeCount += 1
        elif try_damping(x):
            safeCount += 1

    print("Safe :",safeCount)
    return None


if __name__ == "__main__":
    main()