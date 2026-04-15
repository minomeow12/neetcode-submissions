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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        //handle if list1 or list2 exist
        //if (!list1) return list2;
        //if (!list2) return list1;

        //ListNode * head = nullptr;
        //determine the head first
        //if (list1 -> val < list2 -> val)
        //{
        //   head = list1;
         //   list1 = list1 -> next;
        //}
        //else
        //{
        //    head = list2;
        //    list2 = list2 -> next;
        //}

        //ListNode * curr = head;
        //while (list1 && list2)
        //{
        //    if (list1 -> val < list2 -> val)
        //    {
        //        curr -> next = list1;
        //        list1 = list1 -> next;
        //    }
        //    else
        //    {
        //        curr -> next = list2;
        //        list2 = list2 -> next;
        //    }
        //    curr = curr -> next;
        //}
        
        //attach the remaining
        //if (list1)
        //{
        //    curr -> next = list1;
        //}
        //else 
        //{
        //    curr -> next = list2;
        //}
        //return head;
        //ListNode dummy ={0};
        //ListNode * current = &dummy;
        //while (list1 && list2)
        //{
        //    if (list1 -> val < list2 -> val) 
        //    {
        //        current -> next = list1;
        //        list1 = list1 -> next;
        //    }
        //    else
        //    {
        //        current -> next = list2;
        //        list2 = list2 -> next;
        //    }
        //    current = current -> next;
        //}
        //if (list1)
        //{
        //    current -> next = list1;
        //}
        //else
        //{
        //    current -> next = list2;
        //}
        // dummy.next;
        //recursively
        if (!list1) return list2;
        if (!list2) return list1;
        if (list1 -> val <= list2 -> val)
        {
            list1 -> next = mergeTwoLists(list1->next, list2);
            return list1;
        }
        else
        {
            list2 -> next = mergeTwoLists(list1, list2->next);
            return list2;
        }
    }
};
