// 3853. Merge Close Characters

#include <algorithm>
#include <vector>
#include <string>
#include <print>

using namespace std;

class Solution {
    public:
    string mergeCharacters(string s, int k) {

        int i = 0;

        while (i < s.size()) {

            bool merged = false;

            int limit = min(i + k + 1, (int)s.size());

            for (int j = i + 1; j < limit; j++) {
                if(s[i] == s[j]) {
                    s.erase(j, 1);
                    merged = true;
                    i = max(0, i - k);
                    break;
                }
            }

            if (merged == false) {
                i++;
            }
        }

        return s;
    }
};

struct TestCase {
    string s;
    int k;
    string result;
};

int main() {

    Solution s;

    vector<TestCase> testCases = {
      { "abca", 3, "abc" },
      { "aabca", 2, "abca" },
      { "yybyzybz", 2, "ybzybz" },
      { "hhh", 1, "h" },
    };

    for (TestCase t: testCases) {
        string result = s.mergeCharacters(t.s, t.k);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
