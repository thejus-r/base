// 3819. Rotate Non Negative Elements

#include <algorithm>
#include<vector>
#include<print>

using namespace std;

class Solution {
    public:
    vector<int> rotateElements(vector<int> & nums, int k) {
        vector<int> pos_nums;

        for (int n: nums) {
            if (n >= 0) {
                pos_nums.push_back(n);
            }
        }

        k = pos_nums.size() % k;

        reverse(pos_nums.begin(), pos_nums.end());
        reverse(pos_nums.begin(), pos_nums.begin() + k);
        reverse(pos_nums.begin() + k + 1, pos_nums.end());

        println("{}", pos_nums);


        return nums;
    }

};

struct TestCase {};
