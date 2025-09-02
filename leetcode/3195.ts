// Leetcode: 3195
// Find the Minimum Areat to Cover ALl Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i
// #medium

function minimunSum(grid: number[][]): number {
  let m = grid.length;
  let n = grid[0]?.length!;
  let t = m;
  let b = -1;
  let l = n;
  let r = -1;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i]![j] == 1) {
        t = Math.min(t, i);
        b = Math.max(b, i);
        l = Math.min(l, j);
        r = Math.max(r, j);
      }
    }
  }
  return (b - t + 1) * (r - l + 1);
}

let grid = [
  [1, 0, 1],
  [1, 1, 1],
];
let result = minimunSum(grid);
console.log("Example 1", result); // 6

grid = [
  [1, 0],
  [0, 0],
];
result = minimunSum(grid);
console.log("Example 2", result); // 1
