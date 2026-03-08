// 827. Making A Large Island
// Hard

#include <climits>
#include <unordered_map>
#include <algorithm>
#include <unordered_set>
#include <utility>
#include <vector>
#include <print>

using namespace std;

class Solution {
    private:
        vector<pair<int, int>> dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
        int ROWS;
        int COLS;

    public:
    int dfs(int r, int c, int id, vector<vector<int>> &grid) {

        // check bounds
        if (r >= 0 && c >= 0 && r < ROWS && c < ROWS && grid[r][c] != id && grid[r][c] != 0) {
            grid[r][c] = id;

            int area = 1;
            area += dfs(r + 1, c, id, grid);
            area += dfs(r - 1, c, id, grid);
            area += dfs(r, c + 1, id, grid);
            area += dfs(r, c - 1, id, grid);

            return area;
        }

        return 0;
    }

    int largestIsland(vector<vector<int>>& grid) {
        ROWS = grid.size();
        COLS = grid[0].size();

        // id, area
        unordered_map<int, int> islandArea;

        int max_area = INT_MIN;

        // Group islands
        int id = 2;
        for (int r = 0; r < ROWS; r ++){
            for (int c = 0; c < COLS; c ++) {
                if (grid[r][c] == 1) {
                    int area = dfs(r, c, id, grid);
                    max_area = max(max_area, area);
                    islandArea[id] = area;
                    id++;
                }
            }
        }

        // Max area by connecting one zero
        for (int r = 0; r < ROWS; r ++){
            for (int c = 0; c < COLS; c ++) {
                if (grid[r][c] == 0) {
                    // check 4 direactions
                    unordered_set<int> seenIslands;
                    int area = 1;
                    for (auto [dr, dc]: dirs) {
                        int nr = r + dr, nc = c + dc;
                        if (nr >= 0 && nc >= 0 && nr < ROWS && nc < COLS && grid[nr][nc] > 1) {
                            int id = grid[nr][nc];

                            if (!seenIslands.contains(id)) {
                                seenIslands.insert(id);
                                area += islandArea[id];
                            }
                        }
                    }

                    max_area = max(max_area, area);
                }
            }
        }

        return max_area;
    }
};

struct TestCase {
    vector<vector<int>> grid;
    int result;
};

int main() {
    vector<TestCase> testCases = {
        // { { { 1, 0 }, { 0, 1 } }, 3},
        { { { 1, 1 }, { 1, 0 } }, 4},
    };

    Solution s;
    for (TestCase t: testCases) {
        auto result = s.largestIsland(t.grid);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
