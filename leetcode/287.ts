// Leetcode: 287
// Find the Duplicate Number
// https://leetcode.com/problems/find-the-duplicate-number

// Solution Concept : Cyclic Sort
function findDuplicate(nums: number[]): number {
  let i = 0;
  while (i < nums.length) {
    const correct = nums[i]! - 1;
    if (i < nums.length && nums[i] != nums[correct]) {
      const temp = nums[i]!;
      nums[i] = nums[correct]!;
      nums[correct] = temp;
    } else {
      i++;
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != i + 1) {
      return nums[i]!;
    }
  }

  return nums.length;
}

console.log("Example 1 :", findDuplicate([1, 3, 4, 2, 2])); // 2
console.log("Example 2 :", findDuplicate([3, 1, 3, 4, 2])); // 3
console.log("Example 3 :", findDuplicate([3, 3, 3, 3, 3])); // 3
