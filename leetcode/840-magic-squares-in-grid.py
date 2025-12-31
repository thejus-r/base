# 840. Magic Squares In Grid
# Medium


def numMagicSquaresInside(grid: list[list[int]]) -> int:
    R, C = len(grid) - 2, len(grid[0]) - 2
    count = 0

    for r in range(R):
        for c in range(C):
            found = True
            dSum1 = sum([grid[r][c], grid[r + 1][c + 1], grid[r + 2][c + 2]])
            dSum2 = sum([grid[r + 2][c], grid[r + 1][c + 1], grid[r][c + 2]])

            if dSum1 != dSum2:
                found = False

            if found:
                # row sum
                for i in range(3):
                    if dSum1 != sum(grid[r + i][c : c + 3]):
                        found = False
                        break

            if found:
                # col sum
                for i in range(3):
                    if dSum1 != sum(
                        [grid[r][c + i], grid[r + 1][c + i], grid[r + 2][c + i]]
                    ):
                        found = False
                        break

            if found:
                s = set()
                for i in range(r, r + 3):
                    for j in range(c, r + 3):
                        if 1 <= grid[i][j] <= 9:
                            s.add(grid[i][j])

                if len(s) != 9:
                    found = False

            if found:
                count += 1

    return count


print(f"Example 1: {numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]])}")
print(f"Example 2: {numMagicSquaresInside([[8]])}")
print(f"Example 3: {numMagicSquaresInside([[5, 5, 5], [5, 5, 5], [5, 5, 5]])}")
