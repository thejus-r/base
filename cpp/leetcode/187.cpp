// 187. Repeated DNA Sequences

#include <unordered_set>
#include <vector>
#include <string>
#include <print>

using namespace std;

class Solution {
    public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_set<string> seen;
        unordered_set<string> result;

        for (int i = 0; i + 9 < s.length(); i++) {
            string sub = s.substr(i, 10);

            if (seen.count(sub))  {
                result.insert(sub);
            }

            seen.insert(sub);
        }

        return vector<string>(result.begin(), result.end());

    }
};

struct TestCase {
    string s;
    vector<string> result;
};

int main() {
    vector<TestCase> testCases = {
        { "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", { "AAAAACCCCC", "CCCCCAAAAA" } },
        { "AAAAAAAAAAAAA", { "AAAAAAAAAA" } },
    };

    Solution s;

    for (TestCase t: testCases) {
        auto result = s.findRepeatedDnaSequences(t.s);
        println("Expected: {}, Got: {}", t.result, result);
    }

}
