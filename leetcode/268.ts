// Leetcode: 268
// Missing Number
// https://leetcode.com/problems/missing-number

import { expect, test } from "vitest";

// Solution Concept : Cyclic Sort
function missingNumber(nums: number[]): number {
  let i = 0;

  while (i < nums.length) {
    const correct = nums[i]!;
    if (nums[i]! < nums.length && nums[i]! != nums[correct]) {
      const temp = nums[correct]!;
      nums[correct] = correct;
      nums[i] = temp;
    } else {
      i++;
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != i) {
      return i;
    }
  }

  return nums.length;
}

// if (import.meta.vitest) {
test("Example 1", () => {
  const nums = [1, 0, 3, 4];
  expect(missingNumber(nums)).toBe(2);
});

test("Example 2", () => {
  const nums = [1, 0];
  expect(missingNumber(nums)).toBe(2);
});
