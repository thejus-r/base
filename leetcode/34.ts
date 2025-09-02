// Leetcode: 34
// Find First and Last Position of Element in Sorted Array
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
// #medium

function searchRange(nums: number[], target: number): number[] {
  function binarySearch(leftBias: boolean): number {
    let l = 0;
    let r = nums.length - 1;

    let i = -1;

    while (l <= r) {
      let m = Math.floor((l + r) / 2);
      if (target > nums[m]!) {
        l = m + 1;
      } else if (target < nums[m]!) {
        r = m - 1;
      } else {
        i = m;
        if (leftBias) {
          r = m - 1;
        } else {
          l = m + 1;
        }
      }
    }

    return i;
  }

  const left = binarySearch(true);
  const right = binarySearch(false);

  return [left, right];
}

let nums = [5, 7, 7, 8, 8, 10];
let target = 8;
let result = searchRange(nums, target);
console.log("Example 1: ", result);

nums = [5, 7, 7, 8, 8, 10];
target = 6;
result = searchRange(nums, target);
console.log("Example 2: ", result);

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 11, 12];
target = 11;
result = searchRange(nums, target);
console.log("Example 3: ", result);
