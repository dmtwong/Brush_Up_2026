//============================================================================
// Name        : subtract.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stack>
#include <queue>
#include <map>
#include <string>
using namespace std;

/*
Given a singly linked list, modify the value of first half nodes such that :
1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,
and so on …
NOTE :
If the length L of linked list is odd, then the first half implies at first floor(L/2) nodes. So, if L = 5, the first half refers to first 2 nodes.
If the length L of linked list is even, then the first half implies at first L/2 nodes. So, if L = 4, the first half refers to first 2 nodes.
Example :
Given linked list 1 -> 2 -> 3 -> 4 -> 5,
You should return 4 -> 2 -> 3 -> 4 -> 5
as
for first node, 5 - 1 = 4
for second node, 4 - 2 = 2

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };
//ListNode* Solution::subtract(ListNode* A) {
ListNode* subtract(ListNode* A) {
	stack<int> s;
	int n = 0;
	int mid = 0;
    int cur;
	ListNode *head = A;

	while(head->next){
		s.push(head->val);
		head = head->next;
		n++;
	}
    s.push(head->val);
    /*
    head = A;
    for (int i = 0; i < n; ++i){
        A->val = s.top();
        s.pop();
	}
	return A;
    */

    mid = (n+1) / 2;
	head = A;

	for (int i = 0; i < mid; ++i){
        head->val = s.top() - head->val;
        s.pop();
        head = head->next;
	}
	return A;
}

