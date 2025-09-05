from typing import List
def read_2d_number_matrix(filename: str) -> List[List[int]]:
    matrix: List[List[int]] = []
    try:
        with open("input.txt") as file:
            for line in file:
                 row_str = line.strip().split()
                 row_int = list(map(int, row_str))
                 matrix.append(row_int)
    except FileNotFoundError:
        print("Error: File not found")
    except ValueError:
        print("Error: Invalid data in file. Ensure all elements are numbers.")

    return matrix


def main() -> None:
    data = read_2d_number_matrix("input.txt")

    # part 1
    left, right = sorted([x[0] for x in data]), sorted([x[1] for x in data])

    sum = 0
    for x, y in zip(left,right):
        sum += abs(x - y)

    print("Part 1: ", sum)

    # part 2
    freq = {}
    for x in left:
        freq[x] = 0

    for x in right:
        if x in freq:
            freq[x] += 1

    sum2 = 0
    for x, y in freq.items():
        if y == 0:
            continue
        sum2 += x * y


    print("Part 2: ", sum2)
    return

if __name__ == "__main__":
    main()
