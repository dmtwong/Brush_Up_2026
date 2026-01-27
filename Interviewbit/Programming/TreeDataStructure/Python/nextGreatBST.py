# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 12:56:54 2026

@author: mingt
"""
'''

Given a BST node, return the node which has value just greater than the given node.

Example:

Given the tree

               100
              /   \
            98    102
           /  \
         96    99
          \
           97
Given 97, you should return the node corresponding to 98 as thats the value just greater than 97 in the tree.

If there are no successor in the tree ( the value is the largest in the tree, return NULL).

Using recursion is not allowed.

Assume that the value is always present in the tree.

PROBLEM APPROACH:

Complete solution in the hint.
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):

'''

def getSuccessor(A, B):
    next_gt = None
    rt = A
    while rt:
        # print('a', rt.val, rt.left, rt.right, next_gt, B)
        if rt.val > B:
            next_gt = rt.val
            rt = rt.left
            # print('b', rt.val, rt.left, rt.right, next_gt)
        else:
            rt = rt.right
            # print('c', rt.val, rt.left, rt.right, next_gt)
    # print('inally', rt.val, rt.left, rt.right, next_gt)
    return next_gt


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
# root.right = TreeNode(6)
# root.right.left = TreeNode(8)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)


getSuccessor(root, B = 3)


''' python 2.7
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        successor = None
        node = A
        while node:
            if node.val == B:
                node = node.right
                while node:
                    successor = node
                    node = node.left
                return successor
            elif node.val > B:
                successor = node
                node = node.left
            else:
                node = node.right
        # This shouldn't happen...
        return successor

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
TreeNode* Solution::getSuccessor(TreeNode* A, int B) {
    TreeNode* temp, *temp1 = NULL;
    if (!A) {
        return A;
    }
    temp = A;
    //std::cout << temp->val << ";";
    while (temp && temp->val != B) {
        if (temp->val < B) {
            temp = temp->right;
        } else {
            temp1 = temp;
            temp = temp->left;
        }
    }
    // Now temp is the node
    if (temp && temp->right) {
        temp = temp->right;
        while (temp->left) {
            temp = temp->left;
        }
        return temp;
    }
    return temp1;
}
'''