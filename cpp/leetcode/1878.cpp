//1878. Get the Biggest Three Rhombus Sums in a Grid

#include <queue>
#include <vector>
#include <print>
#include <unordered_set>

using namespace std;

class Solution {
  public:
    vector<int> getBiggestThree(vector<vector<int>> &grid) {
      int m = grid.size(), n = grid[0].size();

      vector<vector<int>> sum1(m + 1, vector<int>(n + 2, 0));
      vector<vector<int>> sum2(m + 1, vector<int>(n + 2, 0));

      // to store
      priority_queue<int> h;

      // calculate prefix sum
      for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
          sum1[i][j] = sum1[i - 1][j - 1] + grid[i - 1][j - 1];
          sum2[i][j] = sum2[i - 1][j + 1] + grid[i - 1][j - 1];
        }
      }

      for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; i++) {
          h.push(grid[i][j]);

          for (int k = i + 2; k < m; k += 2) {
            int ux = i, uy = j;
            int dx = k, dy = j;

            int lx = (i + k) / 2, ly = i - (k - i) / 2;
            int rx = (i + k) / 2, ry = j + (k - i) / 2;

            if (ly < 0 || ry >= n) {
              break;


              int score = 0;
              score += sum2[lx + 1][ly + 1] - sum2[ux][uy + 2];
              score += sum1[rx + 1][ry + 1] - sum1[ux][uy];
              score += sum1[dx + 1][dy + 1] - sum1[lx][ly];
              score += sum2[dx + 1][dy + 1] - sum2[rx][ry + 2];
              score -= grid[ux][uy] +  grid[dx][dy] + grid[lx][ly] + grid[rx][ry];

              h.push(score);
            }
          }
        }
      }

      unordered_set<int> result;
      while (!h.empty() && result.size() < 3) {
        int score = h.top(); h.pop();
        result.insert(score);
      }


      vector<int> ans;
      for (int n: result) {
        ans.push_back(n);
      }
      return ans;
    }
};

struct TestCase {
  vector<vector<int>> grid;
  vector<int> result;
};

int main() {
  vector<TestCase> testCases = {
    // { { { 3, 4, 5, 1, 3 }, { 3, 3, 4, 2, 3 }, { 20, 30, 200, 40, 10 }, { 1, 5, 5, 4, 1 }, { 4, 3, 2, 2, 5 } }, { 228, 216, 211 } },
    { { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } }, { 20, 9, 8 } },
  };

  Solution s;

  for (TestCase t: testCases) {
    auto result = s.getBiggestThree(t.grid);
    println("Expected: {}, Got: {}", t.result, result);
  }
}
