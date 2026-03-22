// 3875. Construct Uniform Parity Array 1

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
#include <vector>

using namespace std;

class Solution {
public:
  bool uniformArray(vector<int> &nums1) { return true; }
};

struct TestCase {
  vector<int> nums1;
  bool result;
};

int main() {
  vector<TestCase> testCases = {
      {{2, 3}, true},
      {{4, 6}, true},
  };
}
