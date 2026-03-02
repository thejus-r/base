// 3856. Trim Trailing Vowels

#include <string>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    string trimTrailingVowels(string s) {

        string v = "aeiou";

        int i = s.size() - 1;

        while (i >= 0) {
            if (v.contains(s[i])) {
                s.erase(i, 1);
            } else {
                break;
            }
            i --;
        }

        return s;
    }
};

struct TestCase {
    string s;
    string result;
};

int main() {
  Solution s;

  vector<TestCase> testCases = {
    { "idea", "id" },
    { "day", "day" },
    { "aeiou", "" },
  };

  for (TestCase t: testCases) {
      string result = s.trimTrailingVowels(t.s);
      println("Expected: {}, Got: {}", t.result, result);
  }

  return 0;
}
