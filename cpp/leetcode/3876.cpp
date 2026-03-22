// 3876. Construct Uniform Parity Array II

// Parity Condition for Odd Even
// Even +/- Even = Even
// Even +/- Odd = Odd
// Odd +/- Odd = Even

/*
 *  [2, 3] -> odd even, can make all odd (-neg odd numbers)
 *  [4, 6] -> all even
 *
 *  so all Even, all Odd is true, & even of there is atleast one
 *  odd number we can return true
 *
 */
#include <print>
#include <vector>

using namespace std;

class Solution {
public:
  bool uniformArray(vector<int> &nums1) {
    int smallest = nums1[0];
    bool hasOdd = false;

    for (int n : nums1) {
      if (n < smallest) {
        smallest = n;
      }
      if (n % 2 == 1) {
        hasOdd = true;
      }
    }

    if (smallest % 2 == 1) {
      return true;
    }

    return !hasOdd;
  }
};

struct TestCase {
  vector<int> nums1;
  bool result;
};

int main() {
  vector<TestCase> testCases = {
      {{1, 4, 7}, true},
      {{2, 3}, false},
  };

  Solution s;
  for (TestCase t : testCases) {
    auto result = s.uniformArray(t.nums1);
    println("Expected: {}, Got: {}", t.result, result);
  }
}
