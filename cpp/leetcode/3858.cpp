// 3858. Minimum Bitwise OR From Grid

#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    int minimumOR(vector<vector<int>> &grid) {
        int answer = 0;
        int forced_mask = 0;

        for (int bit_pos = 29; bit_pos >= 0; bit_pos--) {

            /*
             * Create a mask with bit mask with bit_pos
             * combined with previous mask
             */
            int bit_mask = forced_mask | (1 << bit_pos);

            /*
             * tries to find, if we avoid the current bit in bit_pos.
             */
            bool can_avoid_bit = true;

            // we interate to all rows
            for (vector<int>& row: grid) {

                bool valid_number = false;
                // we iterate to all nums
                for (int num: row) {
                    if ((num & bit_mask) == 0) {
                        valid_number = true;
                        break;
                    }
                }

                // we are forced to take the bit
                if (valid_number == false)  {
                    can_avoid_bit = false;
                    break;
                }
            }

            if (can_avoid_bit == true) {
                forced_mask = bit_mask;
            } else {
                answer = answer | (1 << bit_pos);
            }
        }
        return answer;
    }
};

struct TestCase {
    vector<vector<int>> grid;
    int result;
};

int main(){

    Solution s;

    vector<TestCase> testCases = {
        { { { 1, 5 }, { 2, 4 } }, 3 },
        { { { 3, 5 }, { 6, 4 } }, 5 },
    };

    for (TestCase t: testCases) {
        int result = s.minimumOR(t.grid);
        println("Expected: {}, Got: {}", t.result, result);
    }

    return 0;
}
