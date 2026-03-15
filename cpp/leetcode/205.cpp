// 205. Isomorphic Strings

#include <vector>
#include <string>
#include <print>

using namespace std;

class Solution {
  public:
    bool isIsomorphic(string &s, string &t) {
      return false;
    }
  
};

struct TestCase {
  string s;
  string t;
  bool result;
};

int main() {

  vector<TestCase> testCases = {
    { "egg", "add", true }, 
  };

  Solution s;

  for (TestCase t: testCases) {
    auto result = s.isIsomorphic(t.s, t.t);
    println("Expected: {}, Got: {}", t.result, result);
  }
}
