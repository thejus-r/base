// 3866. First Unique Even Element

#include <unordered_map>
#include <vector>
#include <print>

using namespace std;

class Solution {
    public:
    int firstUniqueEven(vector<int>& nums){
        unordered_map<int, int> counts;

        for (int n: nums) {
            counts[n]++;
        }

        for (int n: nums) {
            if (n % 2 == 0 && counts[n] == 1) {
                return n;
            }
        }

        return -1;
    }
};

struct TestCase  {
    vector<int> nums;
    int result;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { {3,4,2,5,4,6 }, 2 },
        { { 4, 4}, -1 },
        { { 10,41,35,50,10,41,34,46,28,38,36 }, 50 },
    };

    for (TestCase t: testCases) {
        int result = s.firstUniqueEven(t.nums);
        println("Expected: {}, Got: {}", t.result, result);
    }
}
