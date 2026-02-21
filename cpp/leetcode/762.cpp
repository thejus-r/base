// 762. Prime Number of Set Bits in Binary Representation

#include <unordered_set>
using namespace std;
class Solution {
    int countSetBits(int n) {
        int count = 0;

        while (n) {
            count += n & 1;
            n >>= 1;
        }
        return count;
    }

    int countPrimeSetBits(int left, int right) {
        unordered_set<int> prime = { 2, 3, 5, 7, 11, 13, 17, 19 };
        int count = 0;

        for (int i = left; i <= right; i ++) {
            int no_of_bits = countSetBits(i);
            if (prime.contains(no_of_bits)) {
                count ++;
            }
        }
        return count;
    }
};
