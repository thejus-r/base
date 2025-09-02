import { isNamedImportBindings } from "typescript";

function twoSum(nums: number[], target: number): number[] {
  let map = new Map();

  let res: number[] = [];

  nums.map((n, i) => {
    if (map.get(n) !== undefined) {
      res = [i, map.get(n)];
    }

    const remainder = target - n;
    map.set(remainder, i);
  });

  return res;
}

let nums = [2, 7, 11, 15];
let target = 9;

console.log("Example 1: ", twoSum(nums, target)); // [0, 1]

nums = [3, 2, 4];
target = 6;

console.log("Example 2: ", twoSum(nums, target)); // [1, 2]

nums = [3, 3];
target = 6;

console.log("Example 3: ", twoSum(nums, target)); // [0, 1]
