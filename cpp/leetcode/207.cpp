// 207. Course Schedule

#include <cassert>
#include <vector>
#include <print>
using namespace std;

/*
* We have to find if the graph is cyclic. If its cyclic, we wont be able to
* complete the course.
*/

class Solution {
    private:
    bool isCyclic(int node, vector<bool>& vis, vector<bool>& path, const vector<vector<int>>& adj) {
        vis[node] = path[node] = true; // mark visited and current path

        for (int next: adj[node]){
            if (!vis[next]) { // not visited
                if (isCyclic(next, vis, path, adj)) {
                    return true; // early return, when found cyclic in recursion
                }
            } else if (path[next]) { // we have already visited this node, in current path
                return true; // detected cycle
            }
        }

        path[node] = false; // revert state for backtracking
        return false; // no cycles is found
    }
    public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<bool> vis(numCourses, false);
        vector<bool> path(numCourses, false);

        for (const vector<int> pre: prerequisites){
            adj[pre[1]].push_back(pre[0]);
        }

        for (int n = 0; n < numCourses; n ++) {
            if (!vis[n] && isCyclic(n, vis, path, adj)) {
                return false;
            }
        }

        return true;
    }
};

struct TestCase {
    int numCourses;
    vector<vector<int>> prerequisites;
    bool expected;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { 2, { { 1, 0 } }, true },
        { 2, { { 0, 1 }, { 1, 0 } }, false },
    };

    for (auto t: testCases) {
        bool result = s.canFinish(t.numCourses, t.prerequisites);
        println("{}",result);
        assert(result == t.expected);
    }
    return 0;
}
