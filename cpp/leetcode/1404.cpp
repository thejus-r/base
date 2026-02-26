// 1404. Number of Steps to Reduce a Number in Binary Representation to One

#include <string>
#include <vector>
#include <print>

using namespace std;
class Solution {
    private:
    void divideByTwo(string &s) { s.pop_back(); }
    void addOne(string &s) {
        int i = s.size() - 1;
        while (i >= 0 && s[i] != '0') {
            s[i] = '0';
            i --;
        }

        if (i < 0) {
            s = '1' + s;
        } else {
            s[i] = 1;
        }
    }
    public:
    int numSteps(string s) {

        int N = s.size();
        int ops = 0;


        while (s.size() > 1) {
            N = s.size();

            if (s[N - 1] == '0') {
                divideByTwo(s);
            } else {
                addOne(s);
            }
            ops++;
        }
        return ops;
    }
};

struct TestCase {
  string s;
  int result;
};

int main() {
    Solution s;

    vector<TestCase> testCases = {
        { "1101", 6 },
        { "10", 1 },
        { "1", 0 },
    };

    for (TestCase t: testCases) {
        int result = s.numSteps(t.s);
        println("Expected: {}, Got: {}",t.result, result);
    }
}
