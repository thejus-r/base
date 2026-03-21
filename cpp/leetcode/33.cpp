// 33. Search in Rotated Sorted Array

#include <print>
#include <vector>

using namespace std;

class Solution {
public:
  int search(vector<int> &nums, int target) {

    // PASS 1: FIND PIVOT
    // Binary Search with right bias

    int left = 0, right = nums.size() - 1;

    while (left < right) {
      int m = left + (right - left) / 2;

      if (nums[m] < nums[right]) {
        right = m;
      } else {
        left = m + 1;
      }
    }
    int pivot = left;

    left = 0, right = nums.size() - 1;
    if (target >= nums[pivot] && target <= nums[right]) {
      left = pivot;
    } else {
      right = pivot + 1;
    }

    while (left <= right) {
      int m = left + (right - left) / 2;

      if (target == nums[m]) {
        return m;
      } else if (target < nums[m]) {
        right = m - 1;
      } else {
        left = m + 1;
      }
    }

    return -1;
  }
};

struct TestCase {
  vector<int> nums;
  int target;
  int result;
};

int main() {
  vector<TestCase> testCases = {

  };

  Solution s;

  for (TestCase t : testCases) {
    auto result = s.search(t.nums, t.target);
    print("Expected: {}, Got: {}", t.result, result);
  }
}
