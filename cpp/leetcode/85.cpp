// 85. Maximal Rectangle

#include <algorithm>
#include <print>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  int maximalRectangle(vector<vector<char>> &matrix) {
    int m = matrix.size(), n = matrix[0].size();
    int max_area = 0;

    // adding 0 at the send to flush out stack
    // in the next pass, aka finding the max area in a histogram
    vector<vector<int>> dp(m, vector<int>(n + 1, 0));

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (i == 0) {
          dp[i][j] = matrix[i][j] == '1' ? 1 : 0;
        } else {
          dp[i][j] = matrix[i][j] == '1' ? 1 + dp[i - 1][j] : dp[i][j];
        }
      }
    }

    // using increasing monotonic stack, can find max area
    for (int i = 0; i < dp.size(); i++) {
      stack<int> s;
      for (int j = 0; j < dp[i].size(); j++) {
        while (!s.empty() && dp[i][s.top()] >= dp[i][j]) {
          int idx = s.top();
          s.pop();

          int w = s.empty() ? j : j - s.top() - 1;
          int area = w * dp[i][idx];
          max_area = max(area, max_area);
        }

        s.push(j);
      }
    }

    return max_area;
  }
};

struct TestCase {
  vector<vector<char>> matrix;
  int result;
};

int main() {

  vector<TestCase> testCases = {{{{'1', '0', '1', '0', '0'},
                                  {'1', '0', '1', '1', '1'},
                                  {'1', '1', '1', '1', '1'},
                                  {'1', '0', '0', '1', '0'}},
                                 6},
                                {{{'1', '0'}, {'1', '0'}}, 2}

  };

  Solution s;
  for (TestCase t : testCases) {
    auto result = s.maximalRectangle(t.matrix);
    println("Expected: {}, Got: {}", t.result, result);
  }
}
