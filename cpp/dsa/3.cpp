// Longest Common Substring

#include <string>
#include <vector>
#include <print>

using namespace std;

class Solution {
  public:
  int longestCommonSubString(string s, string t) {
      return 0;
  }
};

struct TestCase {
    string s;
    string t;
    int expected;
};

int main() {
    vector<TestCase> testCases = {
        { "abcde", "abfce", 2 },
        { "abcdxyz", "xyzabcd", 4 },
    };
}
