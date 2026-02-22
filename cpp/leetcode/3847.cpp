// 3847. Find the Score Difference in a Game

#include <vector>
using namespace std;

class Solution {
    public:
    int scoreDifference(vector<int> & nums ) {
        vector<int> score = { 0, 0 };
        int current = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (i % 2 != 0) {
                current = current == 0 ? 1 : 0;
            }

            if ((i + 1) % 6 == 0) {
                current = current == 0 ? 1 : 0;
            }
            score[current] += nums[i];
        }
        return score[0] - score[1];
    }
};
