// 433. Minimum Genetic Mutation

#include <cassert>
#include <queue>
#include <unordered_set>
#include <vector>
#include <string>
#include <print>

using namespace std;

class Solution {
    public:
        int minMutation(string startGene, string endGene, vector<string>& bank) {
            // only unique genes in
            unordered_set<string> b (bank.begin(), bank.end());
            unordered_set<string> visited;

            queue<pair<string, int>> q;
            q.push({ startGene, 0 });
            visited.insert(startGene);

            int depth = 0;

            while (!q.empty()) {
                auto [curr, d] = q.front(); q.pop();

                if (curr == endGene) {
                    return d;
                }


                for (int i = 0; i < 8; i ++) {
                    char prevChar = curr[i];
                    for (char c: vector<char>({ 'A', 'C', 'G', 'T' })) {
                        curr[i] = c;
                        if (b.find(curr) != b.end() and visited.find(curr) == visited.end()) {
                            visited.insert(curr);
                            q.push({ curr, d + 1 });
                        }
                    }
                    curr[i] = prevChar;
                }
            }
            return -1;
        }
};

struct TestCase {
  string startGene;
  string endGene;
  vector<string> bank;
  int expected;
};

int main() {

    vector<TestCase> testCases = {
        { "AACCGGTT", "AACCGGTA", { "AACCGGTA" }, 1 },
        { "AACCGGTT", "AAACGGTA", { "AACCGGTA", "AACCGCTA", "AAACGGTA" }, 2 },
        { "AAAAAAAA", "ACAAAAAA", { "CAAAAAAA", "CCAAAAAA", "ACAAAAAA" }, 1 },
    };

    Solution s;
    for (auto t: testCases) {
        int result = s.minMutation(t.startGene, t.endGene, t.bank);
        println("{}", result);
        assert(result == t.expected);
    }

}
