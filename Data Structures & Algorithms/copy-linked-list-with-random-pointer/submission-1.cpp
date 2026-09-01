/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head){
            return nullptr;
        }
        Node res = Node(0);
        Node* dummy = &res;
        unordered_map<Node*, Node*> randomConnRecord;

        while (head != nullptr){
            if (!randomConnRecord.count(head)){
                dummy->next = new Node(head->val);
                randomConnRecord[head] = dummy->next;
            }
            else {
                dummy->next = randomConnRecord[head];
            }
            if (head->random && !randomConnRecord.count(head->random)){
                dummy->next->random = new Node(head->random->val);
                randomConnRecord[head->random] = dummy->next->random;
            }
            else {
                dummy->next->random = randomConnRecord[head->random];
            }
            dummy = dummy->next;
            head = head->next;
        }
        return res.next;
    }
};
