// 3871. Count Commas in Range II

#include <vector>
#include <print>

using namespace std;

class Solution {
  public:
    int countCommas(int n) {
      int comma_count = 0;

      int t = 1000;

      while (n >= t) {
        comma_count += n % t + 1;
        t *= 1000;
      }

      return comma_count;
    }

};

struct TestCase {
  int n;
  int result;
};

int main() {
  vector<TestCase> testCases = {
    { 1002, 3 },
    { 998, 0 },
    { 10043, 44 },
  };

  Solution s;

  for (TestCase t: testCases) {
    auto result = s.countCommas(t.n);
    println("Expected: {}, Got: {}", t.result, result);
  }

}
