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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carryBit = 0;
        ListNode res(0);
        ListNode* current = &res;
        while (l1 != nullptr && l2 != nullptr){
            current->next = new ListNode((carryBit + l1->val + l2->val) % 10);
            carryBit = (carryBit + l1->val + l2->val) / 10;
            l1 = l1->next;
            l2 = l2->next;
            current = current->next;
        }
        while (l1 != nullptr) {
            current->next = new ListNode((carryBit + l1->val) % 10);
            carryBit = (carryBit + l1->val) / 10;
            l1 = l1->next;
            current = current->next;
        }
        while (l2 != nullptr) {
            current->next = new ListNode((carryBit + l2->val) % 10);
            carryBit = (carryBit + l2->val) / 10;
            l2 = l2->next;
            current = current->next;
        }
        if (carryBit > 0) {
            current->next = new ListNode(carryBit);
            current = current->next;
            return res.next;
        }
        current->next = nullptr;
        return res.next;
    }
};
