// 4. Median of Two Sorted Arrays

#include <algorithm>
#include <climits>
#include <print>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {

    // ensure nums1 is always the smallest array
    if (nums1.size() > nums2.size()) {
      swap(nums1, nums2);
    }

    int x = nums1.size();
    int y = nums2.size();

    int half = (x + y + 1) / 2;

    int left = 0, right = x;

    while (left <= right) {
      int i = left + (right - left) / 2; // no of elements from nums1
      int j = half - i;                  // no of elements from nums2

      int a_left = (i == 0) ? INT_MIN : nums1[i];
      int a_right = (i == x) ? INT_MAX : nums1[i + 1];

      int b_left = (j == 0) ? INT_MIN : nums2[j];
      int b_right = (j == y) ? INT_MAX : nums2[j + 1];

      if (a_left <= b_right && b_left <= a_right) {
        // found good partition
        if ((x + y) % 2 == 1) {
          // odd
          return 1.0 * max(a_left, a_right);
        } else {
          // even
          return (max(a_left, b_left) + min(a_right, b_right)) / 2.0;
        }
      } else if (a_left > b_right) {
        right = i - 1;
      } else {
        left = i + 1;
      }
    }

    // fallback
    return 0.0;
  }
};

struct TestCase {
  vector<int> nums1;
  vector<int> nums2;
  double result;
};

int main() {
  vector<TestCase> testCases = {

  };

  Solution s;

  for (TestCase t : testCases) {
    auto result = s.findMedianSortedArrays(t.nums1, t.nums2);
    print("Expected: {}, Got: {}", t.result, result);
  }

  return 0;
}
