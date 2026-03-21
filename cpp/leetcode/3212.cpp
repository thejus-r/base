// 3212. Count Submatrices With Equal Frequency of X and Y

#include <print>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  int numberOfSubmatrices(vector<vector<char>> &grid) {
    int count = 0;
    int m = grid.size(), n = grid[0].size();
    vector<vector<pair<int, int>>> p(m + 1,
                                     vector<pair<int, int>>(n + 1, {0, 0}));

    for (int i = 1; i <= m; i++) {
      for (int j = 1; j <= n; j++) {
        p[i][j].first =
            p[i - 1][j].first + p[i][j - 1].first - p[i - 1][j - 1].first;
        p[i][j].second =
            p[i - 1][j].second + p[i][j - 1].second - p[i - 1][j - 1].second;

        if (grid[i - 1][j - 1] == 'X') {
          p[i][j].first += 1;
        }

        if (grid[i - 1][j - 1] == 'Y') {
          p[i][j].second += 1;
        }

        if (p[i][j].first != 0 && p[i][j].second != 0 &&
            p[i][j].first == p[i][j].second) {
          count += 1;
        }
      }
    }
    return count;
  }
};

struct TestCase {
  vector<vector<char>> grid;
  int result;
};

int main() {
  vector<TestCase> testCases = {
      {{{'X', 'Y', '.'}, {'Y', '.', '.'}}, 3},
      {{{'X', 'X'}, {'X', 'Y'}}, 0},
      {{{'.', '.'}, {'.', '.'}}, 0},
  };

  Solution s;

  for (TestCase t : testCases) {
    auto result = s.numberOfSubmatrices(t.grid);
    println("Expected: {}, Got: {}", t.result, result);
  }
}
