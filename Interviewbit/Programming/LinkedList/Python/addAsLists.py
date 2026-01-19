# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 16:22:08 2026

@author: USER
"""

# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#     342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None

# class Solution:
# 	# @param A : head node of linked list
# 	# @param B : head node of linked list
# 	# @return the head node in the linked list
# 	def addTwoNumbers(self, A, B):

# temp = [1,2,3]
# temp.reverse()
# str_temp = ''.join([str(i) for i in temp])
# str_temp

def addTwoNumbers(A, B):
    list_A = list()
    list_B = list()
    while(A):
        list_A.append(A.val)
        A = A.next 
    while(B):
        list_B.append(B.val)
        B = B.next 
    num_1, num_2 = 0, 0 
    if len(list_A) != 0:
        list_A.reverse()
        num_1 = int(''.join([str(i) for i in list_A]))
    if len(list_B) != 0:
        list_B.reverse()
        num_2 = int(''.join([str(i) for i in list_B]))
    result = num_1 + num_2
    result_1 = list(str(result))
    result_1 = [int(i) for i in result_1]
    result_1.reverse()
    n_result = len(result_1)
    
    head_result = ListNode(0)
    curr = head_result
    for i in range(n_result):
        new = ListNode(result_1[i])
        curr.next = new
        curr = new
    return head_result.next
    
# C++
# ListNode* Solution::addTwoNumbers(ListNode* A, ListNode* B) {
#     int carry = 0, temp;
#     ListNode* ret = NULL, *tempNode = NULL, *prev = NULL;
#     assert(A!= NULL || B != NULL);
#     /*
#     if (!A) {
#         return B;
#     }
#     if (!B) {
#         return A;
#     }
#     */
#     ListNode *tmp = A;
#     tmp = tmp -> next;
    
#     while(tmp!= NULL){
#         if(tmp->next == NULL)
#             assert(tmp->val != 0);
#         tmp = tmp -> next;    
#     }
    
#     tmp = B;
#     tmp = tmp -> next;
    
#     while(tmp!= NULL){
#         if(tmp->next == NULL)
#             assert(tmp->val != 0);
#         tmp = tmp -> next;    
#     }
    
#     while(A || B) {
#         temp = carry + (A?A->val:0) + (B?B->val:0);
#         carry = temp/10;
#         temp = temp%10;
#         tempNode = new ListNode(temp);
        
#         if (ret) {
#             prev->next = tempNode;
#         } else {
#             ret = tempNode;
#         }
#         prev = tempNode;
#         if (A) A = A->next;
#         if (B) B = B->next;
#     }
#     if (carry > 0) {
#         tempNode->next = new ListNode(carry);
#     }
#     return ret;    
# }

# Scala:
# /*
#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }
# */
# class Solution {
#     def addTwoNumbers(A: ListNode, B: ListNode): ListNode  = {
#       var res = new ListNode(0)
#       val ret = res
#       var node1 = A
#       var node2 = B
#       var rem = 0
#       while (node1 != null || node2 != null) {
#         val aa = if (node1 == null) 0 else node1.value
#         val bb = if (node2 == null) 0 else node2.value
#         var sum = aa + bb + rem
#         if (sum >= 10) {
#           sum = sum - 10
#           rem = 1
#         } else {
#           rem = 0
#         }
    
#         if (node1 != null) node1 = node1.next
#         if (node2 != null) node2 = node2.next
    
#         val over = node1 == null && node2 == null
#         if (over) {
#           res.value = sum
#           if(rem > 0) {
#             res.next = new ListNode(rem)
#           }
#         } else {
#           res.value = sum
#           res.next = new ListNode(0)
#           res = res.next
#         }
#       }
#       ret
#     }
# }

# # GO
# func addTwoNumbers(a, b *listNode) *listNode {
# 	if a == nil || b == nil {
# 		return nil
# 	}
# 	current := &listNode{}
# 	head := current
# 	rem := 0
# 	for a != nil || b != nil {
# 		data := rem
# 		if a != nil {
# 			data += a.value
# 			a = a.next
# 		}
# 		if b != nil {
# 			data += b.value
# 			b = b.next
# 		}
# 		if data > 9 {
# 			rem = 1
# 			data %= 10
# 		} else {
# 			rem = 0
# 		}
# 		current.next = &listNode{
# 			value: data,
# 		}
# 		current = current.next
# 	}

# 	if rem > 0 {
# 		current.next = &listNode{
# 			value: rem,
# 		}
# 	}

# 	return head.next
# }