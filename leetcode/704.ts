// Leetcode: 704
// Binary Search
// https://leetcode.com/problems/binary-search/
// #easy

function search(nums: number[], target: number): number {
  function binarySearch(lo: number, hi: number) {
    if (hi >= lo) {
      let mid = lo + Math.floor((hi - lo) / 2);

      if (nums[mid] === target) {
        return mid;
      }
      if (nums[mid]! > target) {
        return binarySearch(lo, mid - 1);
      }
      return binarySearch(mid + 1, hi);
    }
    return -1;
  }

  return binarySearch(0, nums.length - 1);
}

let nums = [-1, 0, 3, 5, 9, 12];
let target = 9;
let result = search(nums, target);
console.log("Example 1: ", result);

nums = [-1, 0, 3, 5, 9, 12];
target = 2;
result = search(nums, target);
console.log("Example 2: ", result);
