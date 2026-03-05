// 1582. Special Positions in a Binary Matrix

#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
        int numSpecial(vector<vector<int>> &mat) {

            int rows = mat.size(), cols = mat[0].size();

            vector<int> rowCount(rows, 0);
            vector<int> colCount(cols, 0);

            for (int r = 0; r < rows; r ++) {
                for (int c = 0; c < cols; c++) {
                    if (mat[r][c] == 1){
                        rowCount[r]++;
                        colCount[c]++;
                    }

                }
            }

            int count = 0;
            for (int r = 0; r < rows; r++) {
                for (int c = 0; c < cols; c++) {
                    if (mat[r][c] == 1) {
                        if (rowCount[r] == 1 && colCount[c] == 1) {
                            count++;
                        }
                    }
                }
            }

            return count;

        }

};

struct TestCase {
    vector<vector<int>> mat;
    int result;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { { { 1, 0, 0 }, { 0, 0, 1 }, { 1, 0, 0 } }, 1 },
        { { { 1, 0, 0 }, { 0, 1, 0 }, { 0, 0, 1 } }, 3 },
    };

    for (TestCase t: testCases) {
        auto result = s.numSpecial(t.mat);
        println("Expected: {}, Got: {}", t.result, result);
    }

    return 0;
}
