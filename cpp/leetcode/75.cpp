// 75. Sort Colors

#include <map>
#include <vector>

using namespace std;

class Solution {
    public:
    void sortColors(vector<int>& nums) {
        map<int, int> count = {};

        for (int n: nums) {
            count[n]++;
        }

        int i = 0;
        for (auto [k, v]: count) {
            for (int j = 0; j < v; j ++)  {
                nums[i] = k;
                i ++;
            }
        }
    }

};
