//============================================================================
// Name        : intersectLinkList.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
/*
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	struct ListNode {
		  int val;
		  ListNode *next;
		  ListNode(int x) : val(x), next(NULL) {}
	}
	return 0;
}
*/

/*
 * Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.
Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Problem approach completely explained :

Complete code in the hints section.
 *
 */
struct ListNode {
	  int val;
	  ListNode *next;
	  ListNode(int x) : val(x), next(NULL) {}
};

// ListNode* Solution::getIntersectionNode(ListNode* A, ListNode* B) {
ListNode* getIntersectionNode(ListNode* A, ListNode* B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
        ListNode *ptrA = A;
        ListNode *ptrB = B;

        while (ptrA != ptrB) {
            ptrA = ptrA ? ptrA->next : B;
            ptrB = ptrB ? ptrB->next : A;
        }
        return ptrA;


}

/*
 *
 * ListNode* Solution::getIntersectionNode(ListNode* A, ListNode* B) {
    int lenA = 0, lenB = 0, tempLen, j;
    ListNode *A_temp = A;
    ListNode *B_temp = B;
    ListNode *temp;
    while (A_temp) {
        ++lenA;
        A_temp = A_temp->next;
    }
    while (B_temp) {
        ++lenB;
        B_temp = B_temp->next;
    }
    if (lenA > lenB) {
        tempLen = lenA;
        lenA = lenB;
        lenB = tempLen;
        temp = A;
        A = B;
        B = temp;
    }
    j = 0;
    while (j < lenB - lenA) {
        B = B->next;
        ++j;
    }
    while (A && B) {
        if (A == B) {
            return A;
        } else {
            A = A->next;
            B = B->next;
        }
    }
    return NULL;
}
 */

/*
	def getIntersectionNode(self, A, B):
		la = self.length(A)
		lb = self.length(B)

		a = A
		b = B
		while a and b:
			if la > lb:
				la -= 1
				a = a.next
			elif la < lb:
				lb -= 1
				b = b.next
			else:
				if a == b:
					return a
				else:
					a = a.next
					b = b.next

		return None
 *
 */
