// 127. Word Ladder

#include <cassert>
#include <queue>
#include <string>
#include <unordered_set>
#include <vector>
#include <print>

using namespace std;

class Solution {
  public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> bank(wordList.begin(), wordList.end());
        unordered_set<string> visited;

        queue<pair<string, int>> q;

        q.push({ beginWord, 0 });
        visited.insert(beginWord);

        while (!q.empty()) {
            auto [curr, d] = q.front(); q.pop();

            if (curr == endWord) {
                println("{}", visited);
                return d + 1;
            }

            for (int i = 0; i < curr.size(); i++ ) {
                char prevChar = curr[i];
                for (char c = 'a'; c <= 'z'; c++) {
                    curr[i] = c;
                    if (bank.find(curr) != bank.end() && visited.find(curr) == visited.end()) {
                        visited.insert(curr);
                        q.push({ curr, d + 1 });
                    }
                }
                curr[i] = prevChar;
            }
        }

        return 0;
    }
};

struct TestCase {
    string beginWord;
    string endWord;
    vector<string> wordList;
    int expected;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { "hit", "cog", { "hot", "dot", "dog", "lot", "log", "cog" }, 5 },
        { "hit", "cog", { "hot", "dot", "dog", "lot", "log" }, 0 },
    };

    for (auto t: testCases) {
        int result = s.ladderLength(t.beginWord, t.endWord, t.wordList);
        println("{}", result);
        assert(result == t.expected);
    }
}
