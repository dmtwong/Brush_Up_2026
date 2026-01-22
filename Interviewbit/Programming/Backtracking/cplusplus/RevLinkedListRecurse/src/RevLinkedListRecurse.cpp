//============================================================================
// Name        : RevLinkedListRecurse.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stack>
#include <string>
using namespace std;

/*
 * Reverse a linked list using recursion.

Example :
 Given 1->2->3->4->5->NULL,

return 5->4->3->2->1->NULL.

Constraints:

The number of nodes in the list is the range [0, 5000].

-5000 <= Node.val <= 5000
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}

 */

// Definition for singly-linked list.
struct ListNode {
	int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//ListNode* Solution::reverseList(ListNode* A) {
ListNode* reverseList(ListNode* A) {
	stack<int> s;
	int cur;
	int n = 0;
	ListNode *head = A;
	while(head->next){
		s.push(head->val);
		head = head->next;
		n++;
	}
    s.push(head->val);

	head = A;
	for (int i = 0; i <= n; i++){
        head->val = s.top();
        s.pop();
        head = head->next;
	}
	return A;
}

/*
 /**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };

ListNode* Solution::reverseList(ListNode* A) {
    if (!A) {
        return A;
    }
    ListNode *first, *rest;
    first = A;
    rest = first->next;
    if (!rest) {
        return A;
    }
    rest = reverseList(rest);
    first->next->next = first;
    first->next = NULL;
    return rest;
}

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):

        # recursion base case
        if A.next is None:
            return A

        head = self.reverseList(A.next)

        q = A.next
        q.next = A
        A.next = None

        return head

.. Scala:
class Solution {
    def reverseList(A: ListNode): ListNode  = {

        def reverseList(current: ListNode, prev:ListNode): ListNode = {
            if(current.next == null){
                current.next = prev
                current
            } else {
                val next: ListNode = current.next
                current.next = prev
                reverseList(next, current)

            }

        }

        reverseList(A, null)
    }
}

// GO
 *func reverseList(A *listNode )  (*listNode) {
    if A==nil || A.next==nil {
        return A
    }
    curr, next := A, A.next
    newHead:= reverseList(next)
    next.next=curr
    curr.next=nil
    return newHead
}
 *
 */
