// Leetcode: 448
// Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

// Solution Concept : Cyclic Sort
function findDisappearedNumbers(nums: number[]): number[] {
  let res: number[] = [];

  let i = 0;
  while (i < nums.length) {
    const correct = nums[i]! - 1;
    if (i < nums.length && nums[i] != nums[correct]) {
      const temp = nums[correct]!;
      nums[correct] = nums[i]!;
      nums[i] = temp;
    } else {
      i++;
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != i + 1) {
      res.push(i + 1);
    }
  }

  return res;
}

// Test 1
console.log("Example 1 :", findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]));
console.log("Example 2 :", findDisappearedNumbers([1, 1]));
