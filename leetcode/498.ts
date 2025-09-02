// Leetcode: 498
// Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse
// #medium

// Try 1
function findDiagonalOrder(mat: number[][]): number[] {
  const n = mat.length;
  const m = mat[0]!.length;
  let res: number[][] = new Array(m + n).fill([]);
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      const indexSum = i + j;
      if (indexSum % 2 != 0) {
        res[indexSum] = [...res[indexSum]!, mat[i]![j]!];
      } else {
        res[indexSum] = [mat[i]![j]!, ...res[indexSum]!];
      }
    }
  }

  return res.flat();
}

function findDiagonalOrder2(mat: number[][]): number[] {
  if (!mat || mat.length === 0) return [];
  const n = mat.length,
    m = mat[0]!.length;

  let row = 0,
    col = 0;
  let res: number[] = new Array(m * n);
  for (let i = 0; i < n * m; i++) {
    res[i] = mat[row]![col]!;

    if ((col + row) % 2 === 0) {
      if (col === n - 1) row++;
      else if (row === 0) col++;
      else {
        (row--, col++);
      }
    } else {
      if (row === n - 1) col++;
      else if (col === 0) row++;
      else {
        (row++, col--);
      }
    }
  }

  return res;
}

console.log(
  "Example 1 :",
  findDiagonalOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ]),
);
console.log(
  "Example 2 :",
  findDiagonalOrder([
    [1, 2],
    [3, 4],
  ]),
);
