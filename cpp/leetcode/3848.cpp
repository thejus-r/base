// 3848. Check Digitorial Permutation

#include <algorithm>
#include <unordered_map>
#include <vector>
#include <print>
using namespace std;

class Solution {
    private:
    unordered_map<int, int> fact;
    int findFactorial(int n) {
        if (n <= 1)  {
            return 1;
        }

        if (fact.contains(n)) {
            return fact[n];
        }

        int result = n * findFactorial(n - 1);
        fact[n] = result;
        return result;

    }
    public:
    bool isDigitorialPermutation(int n) {
        vector<int> digits;

        int temp = n;

        while (temp) {
            int d = temp % 10;
            digits.push_back(d);
            temp = temp / 10;
        }

        int sum = 0;

        for (int d: digits){
            sum += findFactorial(d);
        }

        sort(digits.begin(), digits.end());

        do {
            int new_num = 0;
            for (int i = 0; i < digits.size(); i++) {
                new_num = (new_num * 10) + digits[i];
            }
            if (new_num == sum) {
                return true;
            }
            println("{}, {}, {}", digits, new_num, sum);

        } while (next_permutation(digits.begin(), digits.end()));

        return false;
    }
};

int main() {

    Solution s;

    int n = 415;

    bool result = s.isDigitorialPermutation(n);
    println("{}", result);
    return 0;
}
