# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 12:12:23 2026

@author: mingt


class TreeNode: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.data = key 

# Function to insert node in tree recursively
def insertNode(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.data < node.data: 
            if root.right is None: 
                root.right = node 
            else: 
                insertNode(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insertNode(root.left, node) 

# Function to print inorder traversal recursively
def inOrderTraversal(root): 
    if root: 
        inOrderTraversal(root.left) 
        print(root.data) 
        inOrderTraversal(root.right) 
"""
'''
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A):

'''

def isValidBST(A):
    def isValid(A, low = float('-inf'), up = float('inf')):
        if not A:
            return True
        val = A.val
        if val <= low:
            return False
        if val >= up:
            return False
        return isValid(A.left, low, val) and isValid(A.right, val, up)
    if isValid(A):
        return 1
    else:
        return 0


'''
bool isBSTUtil(TreeNode *root, int minVal, int maxVal){
     if(root == NULL) return true;
     
     if(root->val > minVal && root->val < maxVal && 
     isBSTUtil(root->left, minVal, root->val) && isBSTUtil(root->right, root->val, maxVal))
     return true;
     else return false;
     // we check if left subtree nodes value in range (minVal to root val)
     // and right subtree nodes value in range (root val to maxVal) recursively
 }
 
int Solution::isValidBST(TreeNode* A) {
    return isBSTUtil(A, INT_MIN, INT_MAX);
}

'''