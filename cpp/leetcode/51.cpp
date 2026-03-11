// 51. N-Queen

#include <unordered_set>
#include <vector>
#include <string>
#include <print>

using namespace std;

class Solution {
    int n;
    unordered_set<int> col;
    unordered_set<int> posDiag;
    unordered_set<int> negDiag;
    public:

    void solve(int r, vector<string> &board, vector<vector<string>> &res) {
        if (r == n) {
            res.push_back(board);
            return;
        }

        for (int c = 0; c < n; c++) {
            int d1 = r + c;
            int d2 = r - c;
            if (col.contains(c) || posDiag.contains(d1) || negDiag.contains(d2)) {
                continue;
            }

            col.insert(c);
            posDiag.insert(d1);
            negDiag.insert(d2);

            board[r][c] = 'Q';

            solve(r + 1, board, res);

            board[r][c] = '.';
            col.erase(c);
            posDiag.erase(d1);
            negDiag.erase(d2);
        }
    }
    vector<vector<string>> solveNQueens(int n) {

        this->n = n;
        vector<vector<string>> res;

        vector<string> board(n, string(n, '.'));

        solve(0, board, res);

        return res;
    }

};

struct TestCase {
  int n;
  vector<vector<string>> result;
};
int main() {
    vector<TestCase> testCases = {
        { 4, { { ".Q..","...Q","Q...","..Q." }, { "..Q.","Q...","...Q",".Q.." } } },
    };

    Solution s;

    for (TestCase t: testCases) {
        auto result = s.solveNQueens(t.n);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
