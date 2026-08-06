// 3345. Smallest Divisible Digit Product Ia
// Easy

// using namespace std;

#include <print>
#include <vector>
class Solution {
public:
  int smallestNumber(int n, int t) {

    for (int i = n; i < n + 100; i++) {
      int current = i;
      int p = 1;

      while (current > 0) {
        int d = current % 10;
        current = current / 10;
        p *= d;
      }

      if (p % t == 0) {
        return i;
      }
    }

    return -1;
  }
};

struct TestCase {
  int n;
  int k;
  int result;
};

int main() {

  Solution s;

  std::vector<TestCase> testCases = {
      {10, 2, 10},
  };

  for (auto t : testCases) {
    auto result = s.smallestNumber(t.n, t.k);
    std::print("Expected: {}, Got: {}\n", t.result, result);
  }

  return 0;
}
