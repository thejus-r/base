// 329. Longest Increasing Path in a Matrix

#include <cassert>
#include <vector>
#include <print>

using namespace std;

class Solution {

    private:
    int rows, cols;
    vector<pair<int, int>> directions = { { 0, 1 }, { 0, -1 }, { -1, 0 }, { 1, 0 } };
    int memo[205][205];

    int dfs(vector<vector<int>>& matrix, int r, int c) {
        if (memo[r][c] != 0) return memo[r][c];

        int tempAns = 1;

        for (auto [dr, dc]: directions) {
            int nr = r + dr;
            int nc = c + dc;

            if (nr >= 0 && nc >= 0 && nr < rows && nc < cols && matrix[nr][nc] > matrix[r][c]){
                tempAns = max(tempAns, 1 + dfs(matrix, nr, nc));
            }
        }

        return memo[r][c] = tempAns;
    }

    public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        rows = matrix.size();
        cols = matrix[0].size();

        int ans = 0;

        for (int r = 0; r < rows; r ++) {
            for (int c = 0; c < cols; c ++) {
                ans = max(ans, dfs(matrix, r, c));
            }
        }
        return ans;
    }

};

struct TestCase {
    vector<vector<int>> matrix;
    int expected;
};

int main() {

    Solution s;

    vector<TestCase> testCases = {
      { { { 9, 9, 4 }, { 6, 6, 8 }, { 2, 1, 1 } }, 4 },
      { { { 3, 4, 5 }, { 3, 2, 6 }, { 2, 2, 1 } }, 4 },
    };


    for (auto t: testCases) {
        int result = s.longestIncreasingPath(t.matrix);
        println("Expected: {}, Got: {}", t.expected, result);
        assert(result == t.expected);
    }
    return 0;
}
