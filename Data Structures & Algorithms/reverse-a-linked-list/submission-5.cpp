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
    ListNode* reverseList(ListNode* head) {
        if (!head) return nullptr;
        return reverse(head);
    }

    ListNode* reverse(ListNode *& head)
    {
        ListNode * new_head = head;
        if (head -> next)
        {
            new_head = reverse(head->next);
            head -> next -> next = head;
        }
        head -> next = nullptr;
        return new_head;
    }
};

