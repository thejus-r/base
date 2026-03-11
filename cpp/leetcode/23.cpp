// 23. Merge k Sorted Lists

#include <queue>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {


    public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {

        auto comp = [](ListNode* l, ListNode* r) {
            return l->val > r->val;
        };

        priority_queue<ListNode*, vector<ListNode*>, decltype(comp)> minHeap(comp);

        for (ListNode* node: lists) {
            if (node != nullptr) {
                minHeap.push(node);
            }
        }

        ListNode dummy(0);
        ListNode* curr = &dummy;

        while (!minHeap.empty()) {
            ListNode* smallest = minHeap.top();
            minHeap.pop();

            curr->next = smallest;
            curr = curr->next;

            if (smallest->next != nullptr) {
                minHeap.push(smallest->next);
            }
        }

        return dummy.next;
    }
};
