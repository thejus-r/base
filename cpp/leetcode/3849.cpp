// 3849. Maximum Bitwise XOR After Rearrangement

#include <string>
#include <print>
#include <vector>
using namespace std;
class Solution {
  public:
  string maximumXor(string s, string t) {
      int setBits = 0;

      for (int i = 0; i < t.size(); i ++) {
          if (t[i] == '1') {
              setBits ++;
          }
      }
      string res = "";
      for (int i = 0; i < s.size(); i++) {
          if (s[i] == '0' && setBits) {
              res += '1';
              setBits --;
          } else {
              res += '0';
          }
      }

      if (setBits) {
          for (int i = s.size()- 1; i >= 0; i--) {
              if (s[i] == '1' && setBits) {
                  res[i] = '1';
                  setBits--;
              }
          }
      }


      string final = "";

      for (int i = 0; i < s.size(); i++) {
          if (s[i] == res[i]) {
              final += '0';
          } else {
              final += '1';
          }
      }
      return final;
  }
};

struct TestCase {
    string s;
    string t;
    string res;
};

int main() {
    vector<TestCase> testCases = {
      { "101", "011", "110" },
      { "0110", "1110", "1101" },
    };
    Solution s;

    for (TestCase t: testCases) {
        string res = s.maximumXor(t.s, t.t);
    }

    return 0;
}
