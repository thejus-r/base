// 3070. Count Submatrices with Top-Left Element and Sum Less Than k

#include <print>
#include <vector>

using namespace std;

class Solution {
public:
  int countSubmatrices(vector<vector<int>> &grid, int k) {
    int count = 0;

    for (int i = 0; i < grid.size(); i++) {
      for (int j = 0; j < grid[0].size(); j++) {

        int top = (i == 0) ? 0 : grid[i - 1][j];
        int left = (j == 0) ? 0 : grid[i][j - 1];
        int topLeft = (i == 0 || j == 0) ? 0 : grid[i - 1][j - 1];

        grid[i][j] += top + left - topLeft;

        if (grid[i][j] <= k) {
          count++;
        }
      }
    }

    println("DEBUG: {}", grid);
    return count;
  }
};

struct TestCase {
  vector<vector<int>> grid;
  int k;
  int result;
};

int main() {
  vector<TestCase> testCases = {
      {{{7, 6, 3}, {6, 6, 1}}, 18, 4},
      {{{7, 2, 9}, {1, 5, 0}, {2, 6, 6}}, 20, 6},
  };

  Solution s;
  for (TestCase t : testCases) {
    auto result = s.countSubmatrices(t.grid, t.k);
    println("Expected: {}, Got: {}", t.result, result);
  }
}
