// 703. Kth Largest Element in a Stream

#include <functional>
#include <queue>
#include <vector>
#include <print>

using namespace std;

class KthLargest {
    private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

    public:
        KthLargest(int k, vector<int> nums) {
            this->k = k;

            for (int n: nums) {
                q.push(k);
            }
        }

        int add(int val) {
            if (minHeap.size() < k || minHeap.top() < k) {
                minHeap.push(val);

                if (minHeap.size() > k) {
                    minHeap.pop();
                }

            }

            return minHeap.top();
        }

};

int main() {
}
