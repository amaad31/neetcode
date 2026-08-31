/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* node1, ListNode* node2){
        ListNode res = ListNode(0);
        ListNode* dummy = &res;
        while (node1 != nullptr && node2 != nullptr){
            if (node1->val <= node2->val){
                dummy->next = node1;
                node1 = node1->next;
                dummy = dummy->next;
            }
            else {
                dummy->next = node2;
                node2 = node2->next;
                dummy = dummy->next;
            }
        }
        if (node1 != nullptr){
            dummy->next = node1;
        }
        if (node2 != nullptr){
            dummy->next = node2;
        }
        return res.next;
    }
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int listsSize = static_cast<int>(lists.size());
        if (listsSize == 0){
            return {};
        }

        if (listsSize== 1){
            return lists[0];
        }
        vector<ListNode*> mergedLists;
        for (int i = 0; i < listsSize; i = i + 2){
            if (i + 1 < listsSize){
                mergedLists.push_back(mergeTwoLists(lists[i], lists[i + 1]));
            }
            else {
                mergedLists.push_back(mergeTwoLists(lists[i], nullptr));
            }
        }
        return mergeKLists(mergedLists);
    }
};
