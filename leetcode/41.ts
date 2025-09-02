// Leetcode: 41
// First Missing Positive
// https://leetcode.com/problems/first-missing-positive

// Solution Concept: Cyclic Sort
function firstMissingPositive(nums: number[]): number {
  let i = 0;
  while (i < nums.length) {
    const correct = nums[i]! - 1;
    if (nums[correct] !== nums[i] && nums[i]! < nums.length && nums[i]! > 0) {
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
      return i + 1;
    }
  }
  return nums.length + 1;
}

console.log("Example 1 :", firstMissingPositive([1, 2, 0])); // 3
console.log("Example 2 :", firstMissingPositive([3, 4, -1, 1])); // 2
console.log("Example 3 :", firstMissingPositive([7, 8, 9, 11, 12])); // 1
