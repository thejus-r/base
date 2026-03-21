// 34. Find First and Last Position of Element in Sorted Array

#include <vector>

using namespace std;

class Solution {
public:
  int binarySearch(vector<int> &nums, int target, bool leftBias) {
    int left = 0, right = nums.size() - 1;

    int res = -1;

    while (left <= right) {
      int m = left + (right - left) / 2;

      if (target > nums[m]) {
        left = m + 1;
      } else if (target < nums[m]) {
        right = m - 1;
      } else {
        res = m;
        if (leftBias) {
          right = m - 1;
        } else {
          left = m + 1;
        }
      }
    }

    return res;
  }

  vector<int> searchRange(vector<int> &nums, int target) {
    vector<int> res(2, -1);

    res.push_back(binarySearch(nums, target, true));
    res.push_back(binarySearch(nums, target, false));

    return res;
  }
};
