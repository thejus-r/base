// 169. Majority Element

#include <cstdlib>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
    public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> m;

        for (auto num: nums) {
            m[num]++;
        }

        for (auto [k, v]: m) {
            if (v > n / 2) {
                return k;
            }
        }

        return -1;
    }
};
