// 1356. Sort Integers by The Number of 1 Bits

#include <map>
#include <vector>
#include <algorithm>
#include <print>

using namespace std;
class Solution {
    public:
    vector<int> sortByBits(vector<int>& arr) {
        map<int, vector<int>> freq;

        for (int n: arr) {
            int t = n;
            int set_bits = 0;
            while (n) {
                if (n % 2 != 0) {
                    set_bits ++;
                }
                n /= 2;
            }

            freq[set_bits].push_back(t);
        }

        vector<int> result;

        println("{}", freq);

        for (auto [k, v] :freq) {
            sort(v.begin(), v.end());
            result.insert(result.end(), v.begin(), v.end());
        }

        return result;
    }

};

struct TestCase {
    vector<int> arr;
    vector<int> result;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { { 0, 1, 2, 3, 4, 5, 6, 7, 8 }, { 0, 1, 2, 4, 8, 3, 5, 6, 7 } },
        { { 1024,512,256,128,64,32,16,8,4,2,1 }, { 1,2,4,8,16,32,64,128,256,512,1024 } }
    };

    for (TestCase t: testCases) {
        vector<int> result = s.sortByBits(t.arr);
        println("Expected: {}, Got: {}", t.result, result);
    }
    return 0;
}
