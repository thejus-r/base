// Leetcode: 3000
// Maximun Area of Longest Diagonal Rectangle
// https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle
// #easy

function areaOfMaxDiagonal(dimensions: number[][]): number {
  let maxArea = 0,
    maxDiag = 0;

  for (let i = 0; i < dimensions.length; i++) {
    let l = dimensions[i]![0]!;
    let w = dimensions[i]![1]!;
    let currDiag = l * l + w * w;

    if (currDiag > maxDiag || (currDiag === maxDiag && l * w > maxArea)) {
      maxDiag = currDiag;
      maxArea = l * w;
    }
  }
  return maxArea;
}

// console.log(
//   "Example 1: ",
//   areaOfMaxDiagonal([
//     [9, 3],
//     [8, 6],
//   ]),
// );

// console.log(
//   "Example 2: ",
//   areaOfMaxDiagonal([
//     [3, 4],
//     [4, 3],
//   ]),
// );

// console.log(
//   "Example 3: ",
//   areaOfMaxDiagonal([
//     [2, 6],
//     [5, 1],
//     [3, 10],
//     [8, 4],
//   ]),
// );

console.log(
  "Example 4: ",
  areaOfMaxDiagonal([
    [6, 5],
    [8, 6],
    [2, 10],
    [8, 1],
    [9, 2],
    [3, 5],
    [3, 5],
  ]),
);
