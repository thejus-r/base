// Leetcode: 442
// Find all the Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array

// Solution Concept : Cyclic Sort
function findDuplicate(nums: number[]): number[] {
  let i = 0;
  let res: number[] = [];
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
      res.push(nums[i]!);
    }
  }

  return res;
}

console.log("Example 1 :", findDuplicate([4, 3, 2, 7, 8, 2, 3, 1])); // 2
console.log("Example 2 :", findDuplicate([1, 1, 2])); // 3
console.log("Example 3 :", findDuplicate([1])); // 3
