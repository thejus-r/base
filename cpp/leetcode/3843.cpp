// First element with unique frequency

#include <iostream>
#include <unordered_map>
#include <vector>
#include <cassert>

using namespace std;

class Solution {
    public:
        int firstUniqueFreq(vector<int>& nums) {
            int n = nums.size();
            unordered_map<int, int> m1, m2;

            for (int i: nums) {
                m1[i]++;
            }

            for (auto i: m1) {
                m2[i.second]++;
            }

            for (int i = 0; i < n; i++) {
                if (m2[m1[nums[i]]] == 1) {
                    return nums[i];
                }
            }

            return -1;
        };
};

int main() {
    Solution sol;

    vector<int> arr1 = {20,10,30,30};
    int result1 = sol.firstUniqueFreq(arr1);
    assert(result1 == 30);
    cout << "Test 1 Passed! ✅" << endl;

    return 0;
}
