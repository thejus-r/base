// 3842. Toggle Light Bulbs

#include <unordered_map>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
    public:
    vector<int> toggleLightBulbs(vector<int>& bulbs) {
        vector<int> res = {};
        unordered_map<int, int> m;

        for (int b : bulbs) {
            m[b]++;
        }

        for (auto i: m) {
            if (i.second % 2 != 0) {
                res.push_back(i.first);
            }
        }
        sort(res.begin(), res.end());
        return res;
    }
};

int main() {
    Solution s;

    vector<int> bulbs = {10,30,20,10};
    vector<int> expected = {20, 30};
    auto result = s.toggleLightBulbs(bulbs);

    assert(result == expected);
    cout << "Test passed successfully! ✅" << endl;

    return 0;
}
