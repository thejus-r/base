// 542. 01 Matrix

#include <utility>
#include <vector>
#include <queue>
#include <print>

using namespace std;
class Solution {
    public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {

        // row and column numbers
        int rows = mat.size(), cols = mat[0].size();

        // 4 directions of movement
        vector<pair<int, int>> directions = {{ 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 }};

        // max possible distance
        int MAX_VALUE = rows * cols;

        // solve using multi-source bfs
        // finding all sources

        queue<pair<int, int>> q;
        for (int r = 0; r < rows; r ++) {
            for (int c = 0; c < cols; c ++) {
                if (mat[r][c] == 0) {
                    q.push({ r, c });
                } else {
                    mat[r][c] = MAX_VALUE;
                }
            }
        }

        while (!q.empty()) {
            int qLen = q.size();

            for (int i = 0; i < qLen; i++) {
                auto [x, y] = q.front(); q.pop();

                for (auto [dx, dr]: directions) {
                    int nx = x + dx, ny = y + dr;

                    if (isValid(nx, ny, rows, cols) && mat[nx][ny] > mat[x][y] + 1) {
                        q.push({ nx, ny });
                        mat[nx][ny] = mat[x][y] + 1;
                    }
                }
            }
        }
        return mat;
    }

    private:
    bool isValid(int r, int c, int rows, int cols) {
        return (r >= 0 && c >= 0 && r < rows && c < cols);
    }
};

struct TestCase {
    vector<vector<int>> mat;
    vector<vector<int>> expected;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { {{ 0, 0, 0 }, { 0, 1, 0 }, { 0, 0, 0 }}, {{ 0,0,0 }, { 0, 1, 0 }, { 0, 0, 0 }} }
    };

    for (auto t: testCases){
        auto result = s.updateMatrix(t.mat);
        println("{}", result);
    }
}
