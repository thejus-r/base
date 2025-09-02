// Leetcode: 645
// Set Mismatch
// https://leetcode.com/problems/set-mismatch

// Solution Concept: Cyclic Sort
function findErrorNums(nums: number[]): number[] {
  const res: number[] = [];

  let i = 0;
  while (i < nums.length) {
    const correct = nums[i]! - 1;
    if (nums[correct] !== nums[i]) {
      const temp = nums[correct]!;
      nums[correct] = nums[i]!;
      nums[i] = temp;
    } else {
      i++;
    }
  }

  console.log(nums);

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != i + 1) {
      return [nums[i]!, i + 1];
    }
  }

  return [];
}

console.log("Example 1 :", findErrorNums([1, 2, 2, 4])); // [2,3]
console.log("Example 2 :", findErrorNums([1, 1])); // [1,2]
