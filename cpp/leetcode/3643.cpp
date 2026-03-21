// 3643. Flip Square Submatrix Vertically

#include <print>
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> reverseSubmatrix(vector<vector<int>> &grid, int x, int y,
                                       int k) {
    int m = grid.size(), n = grid[0].size();

    for (int j = y; j < y + k; j++) {
      int t = x;
      int b = x + k - 1;

      while (t < b) {
        swap(grid[t][j], grid[b][j]);
        t += 1;
        b -= 1;
      }
    }

    return grid;
  }
};

struct TestCase {
  vector<vector<int>> grid;
  int x, y, k;
  vector<vector<int>> result;
};

int main() {
  vector<TestCase> testCases = {
      {{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}},
       1,
       0,
       3,
       {{1, 2, 3, 4}, {13, 14, 15, 8}, {9, 10, 11, 12}, {5, 6, 7, 16}}}};

  Solution s;

  for (TestCase t : testCases) {
    auto result = s.reverseSubmatrix(t.grid, t.x, t.y, t.k);
    println("Expected: {}, Got: {}", t.result, result);
  }
}
