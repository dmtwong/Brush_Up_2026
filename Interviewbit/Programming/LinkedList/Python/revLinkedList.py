# -*- coding: utf-8 -*-
"""
Created on Sun Jan 18 15:53:38 2026

@author: USER
"""

# Reverse a linked list. Do it in-place and in one-pass.
# For example:
# Given 1->2->3->4->5->NULL,
# return 5->4->3->2->1->NULL.
# PROBLEM APPROACH :
# Complete solution code in the hints

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

# class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
# 	def reverseList(self, A):
def reverseList(A):
    prev = None
    curr = A        
    while curr:
        temp_next = curr.next             
        curr.next = prev            
        prev = curr
        curr = temp_next            
    return prev

'''
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        current = A
        prev = None
        
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        head = prev
        return head
'''

''' C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::reverseList(ListNode* A) {
    ListNode *revA = NULL, *nextA;
    while (A) {
        nextA = A->next;
        A->next = revA;
        revA = A;
        A = nextA;
    }
    return revA;
}


'''

''' Scala:
/*
 * Definition for singly-linked list
 * class ListNode(val xc: Int){
 *     var value: Int = xc
 *     var next: ListNode = null
 * }
*/
class Solution {
    def reverseList(A: ListNode): ListNode  = {
        def reverseList(curr: ListNode, prev: ListNode): ListNode = {
            if (curr.next == null) {
                curr.next = prev
                return curr
            }
 
            val next: ListNode = curr.next
     
            curr.next = prev
     
            return reverseList(next, curr)
            
        }
        reverseList(A, null)
    }
}
'''

# GO
'''
/**
 * Definition for singly-linked list.
 * type listNode struct {
 *     value int
 *     next *listNode
 * }
 * 
 * func listNode_new(val int) *listNode{
 *     var node *listNode = new(listNode)
 *     node.value = val
 *     node.next = nil
 *     return node
 * }
 */
/**
 * @input A : Head pointer of linked list 
 * 
 * @Output head pointer of list.
 */
func reverseList(root *listNode )  (*listNode) {
    if root == nil || root.next == nil {
        return root
    }
    rest := reverseList(root.next)
    root.next.next = root
    root.next = nil
    return rest
}
'''