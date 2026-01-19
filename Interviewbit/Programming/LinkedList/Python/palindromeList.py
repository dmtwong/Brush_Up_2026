# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 17:03:28 2026

@author: USER
"""
# Problem Description
# Given a singly linked list A, determine if it's a palindrome. Return 1 or 0, denoting if it's a palindrome or not, respectively.
# Problem Constraints
#  1 <= |A| <= 105 
# Input Format
# The first and the only argument of input contains a pointer to the head of the given linked list. 
# Output Format
#  Return 0, if the linked list is not a palindrome. 

#  Return 1, if the linked list is a palindrome. 
# Example Input
#  Input 1: 
# A = [1, 2, 2, 1]
# Input 2:
# A = [1, 3, 2]

# Example Output
#  Output 1:  1 
#  Output 2:  0 
# Example Explanation
# Explanation 1:
#  The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.
# Explanation 2:
#  The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

# class Solution:
# 	# @param A : head node of linked list
# 	# @return an integer
# 	def lPalin(self, A):
# 5, mid 2 0,5 1,4, 2,3
# 4, mid 2 0, 1, 
def lPalin(A):
    result = []
    B = A
    while B:
        result.append(B.val)
        B = B.next
    n_A = len(result)
    if n_A % 2 == 1:
        mid = n_A//2 + 1
    else:
        mid = n_A//2
    for i in range(mid):
        if result[i] != result[-(i+1)]:
            return 0
    return 1

# # C++
# ListNode* reverseList(ListNode* A){
#     ListNode* prev=NULL;
#     ListNode* nxt=NULL;
#     while(A){
#         nxt=A->next;
#         A->next=prev;
#         prev=A;
#         A=nxt;
#     }
#     return prev;
# } 
# int Solution::lPalin(ListNode* A) {
#     ListNode* HEAD = A;
#     int size=0;
#     while(A){
#         size++;
#         A=A->next;
#     }
#     int mygo = size/2;
#     A=HEAD;
#     ListNode* TAIL=NULL;
#     if(size%2==0){    
#         while(mygo--){
#             A=A->next;
#         }
#         TAIL = reverseList(A);
#     }
#     else{
#         mygo++;
#         while(mygo--){
#             A=A->next;
#         }
#         TAIL = reverseList(A);
#     }
#     for(int i=0;i<size/2;i++){
#         if(HEAD->val!=TAIL->val) return 0;
#         HEAD = HEAD->next;
#         TAIL = TAIL->next;
#     }
#     return 1;
    
# }
# Editorial:
# class Solution:
#     # @param A : head node of linked list
#     # @return an integer
#     def lPalin(self, A):
#         lenL = 0
#         head = thead = thead2 =A        
#         # Find length of the linked list
#         while head is not None:
#             head = head.next
#             lenL += 1        
#         # Reverse right half of the linked list
#         i = 0
#         prev = None
#         nextNode = thead.next
#         while thead is not None:
#             nextNode = thead.next
#             if i >= (lenL // 2):
#                 thead.next = prev
#             prev = thead
#             thead = nextNode
#             i += 1
#         # Check left and right part of the linked list
#         j = 0
#         while j <= (lenL // 2) and thead2 is not None:
#             if thead2.val != prev.val:
#                 return 0
#             thead2 = thead2.next
#             prev = prev.next
#             j += 1        
#         return 1

# # Scala
# /*
#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }
# */
# class Solution {
#     def lPalin(A: ListNode): Int  = {
#         import scala.collection.mutable.ArrayBuffer

#     var len = 0
#     var n = A
#     while (n != null) {
#       len += 1
#       n = n.next
#     }

#     val fh = (len / 2) - 1
#     val sh = len - 1 - fh

#     n = A
#     var i  = 0
#     val secHalf: ArrayBuffer[Int] = ArrayBuffer()
#     while (n != null) {
#       if (i >= sh) secHalf += n.value
#       i += 1
#       n = n.next
#     }

#     var res = 1
#     n = A
#     for (i <- secHalf.length - 1 to 0 by - 1 if res == 1) {
#       if (secHalf(i) != n.value) res = 0
#       else n = n.next
#     }

#     res
#   }

# }

# # GO
# /**
#  * Definition for singly-linked list.
#  * type listNode struct {
#  *     value int
#  *     next *listNode
#  * }
#  * 
#  * func listNode_new(val int) *listNode{
#  *     var node *listNode = new(listNode)
#  *     node.value = val
#  *     node.next = nil
#  *     return node
#  * }
#  */
# /**
#  * @input A : Head pointer of linked list 
#  * 
#  * @Output Integer
#  */
 
#  //Compare twoLists
# func compareTwoLists(first, second *listNode) int {
#     temp1 := first
#     temp2 := second
#     for temp1 != nil && temp2 != nil {
#         if temp1.value == temp2.value {
#             temp1 = temp1.next
#             temp2 = temp2.next
#         } else {
#             return 0
#         }
#     }

#     if temp1 == nil && temp2 == nil {
#         return 1
#     }

#     return 0
# }

# /* Helper Function to Reverse LinkedList */
# func Reverse(root *listNode) *listNode {
#     if root == nil || root.next == nil {
#         return root
#     }
#     // Reach till end of list and start recursion
#     rest := Reverse(root.next)
#     root.next.next = root
#     root.next = nil
#     return rest
# }

# func lPalin(root *listNode )  (int) {
#     var first, second *listNode
#     fast := root
#     slow := root
#     var middleNode *listNode

#     var prev *listNode
#     if root == nil || root.next == nil{
#         return 1
#     }
#     for fast != nil && fast.next != nil {
#         fast = fast.next.next
#         prev = slow
#         slow = slow.next

#     }

#     //In case of even, fast will be non nil. 
#     if fast != nil {
#         middleNode = slow
#         second = slow.next
#         prev.next = nil
#     } else {
#         second = slow
#         prev.next = nil
#     }

#     first = root
#     secondreversed := Reverse(second)
#     result := compareTwoLists(first, secondreversed)
#     second = Reverse(secondreversed)


#     // Recreate the list
#     if middleNode != nil {
#         prev.next = middleNode
#         middleNode.next = second
#     } else {
#         prev.next = second
#     }

#     return result

# }
