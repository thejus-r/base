// 121. Best Time to Buy and Sell Stock
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;

class Solution {
  public:
  int maxProfit(vector<int> &prices) {
      int buyPrice = prices[0];
      int profit = 0;

      for (int i = 1; i < prices.size(); i++) {
          if (buyPrice > prices[i]) {
              buyPrice = prices[i];
          }
          profit = max(profit, prices[i] - buyPrice);
      }
      return profit;
  }
};

int main() {
    Solution s;

    vector<int> prices1 = {7,1,5,3,6,4};
    int expected1 = 5;

    auto result1 = s.maxProfit(prices1);
    assert(result1 == expected1);
    return 0;
}
