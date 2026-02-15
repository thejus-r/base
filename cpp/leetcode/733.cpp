// 733. Flood Fill

#include <cassert>
#include <utility>
#include <vector>
#include <stack>

using namespace std;

class Solution {

    private:
    bool isValid(int x, int y, int rows, int cols) {
        return (x >= 0 && x < rows && y >= 0 && y < cols);
    }

    public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {

        vector<vector<int>> res = image;
        int rows = image.size(), cols = image[0].size();

        vector<vector<bool>> visited(rows, vector<bool>(cols, false));

        stack<pair<int, int>> st;

        vector<pair<int, int>> directions = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};


        st.push({ sr, sc });
        res[sr][sc] = color;

        while (!st.empty()) {
            pair<int, int> p = st.top();
            st.pop();

            int x=p.first, y=p.second;
            visited[x][y] = true;

            for (auto d: directions) {
                int dx = d.first, dy = d.second;
                int nx = x + dx, ny = y + dy;

                if (isValid(nx, ny, rows, cols) && !visited[nx][ny] && image[x][y] == image[nx][ny]) {
                    res[nx][ny] = color;
                    visited[nx][ny] = true;
                    st.push({ nx, ny });
                }
            }
        }
        return res;
    }
};

struct TestCase {
    vector<vector<int>> image;
    int sr;
    int sc;
    int color;
    vector<vector<int>> expected;
};

int main() {
    vector<TestCase> testCases = {
        {{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}, 1, 1, 2, {{ 2, 2, 2 }, { 2, 2, 0 }, { 2, 0, 1 }}},
        {{{0, 0, 0}, {0, 0, 0}}, 0, 0, 0, {{ 0, 0, 0 }, { 0, 0, 0 }}},
    };

    Solution s;
    for (auto t: testCases) {
        auto result = s.floodFill(t.image, t.sr, t.sc, t.color);
        assert(result == t.expected);
    }
    return 0;
}
