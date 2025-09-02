// Leetcode: 3197
// Find the Minimum Areat to Cover ALl Ones II
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii
// #hard

function minimunSum(grid: number[][]): number {
  return 0;
}

let grid = [
  [1, 0, 1],
  [1, 1, 1],
];
let result = minimunSum(grid);
console.log("Example 1", result); // 5

grid = [
  [1, 0, 1, 0],
  [0, 1, 0, 1],
];
result = minimunSum(grid);
console.log("Example 2", result); // 5
