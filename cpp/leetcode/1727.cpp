// 1727. Largest Submatrix With Rearrangements

#include <print>
#include <vector>

using namespace std;

class Solution {
public:
  int largestSubmatrix(vector<vector<int>> &matrix) {
    int m = matrix.size(), n = matrix[0].size();

    // pre process
    for (int i = 1; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (matrix[i][j] != 0)
          matrix[i][j] += matrix[i - 1][j];
      }
    }

    int max_area = 0;
    for (int i = 0; i < m; i++) {
      sort(matrix[i].rbegin(), matrix[i].rend());
      for (int j = 0; j < n; j++) {
        int area = matrix[i][j] * (j + 1);
        if (area > max_area) {
          max_area = area;
        }
      }
    }
    return max_area;
  }
};

struct TestCase {
  vector<vector<int>> matrix;
  int result;
};

int main() {
  vector<TestCase> testCases = {{{{0, 0, 1}, {1, 1, 1}, {1, 0, 1}}, 4}};

  Solution s;
  for (TestCase t : testCases) {
    auto result = s.largestSubmatrix(t.matrix);
    println("Expected: {}, Got: {}", t.result, result);
  }
}
