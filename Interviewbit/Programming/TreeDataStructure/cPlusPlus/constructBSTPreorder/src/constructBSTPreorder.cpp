//============================================================================
// Name        : constructBSTPreorder.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

/*
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}

Problem Description
Given an integer array A with distinct elements, which represents the preorder traversal of a binary search tree,
construct the tree and return its root.
A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.
A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.
**Problem Constraints**
1 <= |A| <= 105
1 <= A.val <= 109
The given array is a valid preorder traversal of a BST.
**Input Format**
The first argument is an integer array denoting the preorder traversal.
**Output Format**
Return the root of the Binary Search Tree.
**Example Input**
Input 1:
A = [2, 1, 4, 3, 5]
Input 2:
A = [1, 2, 3]
**Example Output**
Output 1:
    2
   / \
  1   4
     / \
    3   5
Output 2:

      1
     /
    2
   /
  3

  */


struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* helper(vector<int>& A, int &ix ,int up) {
	// int ix;
	if (ix == A.size() || A[ix] > up)
		return NULL;
	TreeNode* rt = new TreeNode(A[ix++]);
	rt->left = helper(A, ix, rt->val);
	rt->right = helper(A, ix, up);
	return rt;
}
// TreeNode* Solution::constructBST(vector<int> &A) {
TreeNode* constructBST(vector<int> &A) {
	/*
    int ix_preord = 0;
    int n_A = A.size();
    auto tree = [&](auto& self, int low, int high) -> TreeNode* {
        if (ix_preord >= n_A || A[ix_preord] <= low || A[ix_preord] >= high) {
            return;
        }

        TreeNode* rt = new TreeNode(A[ix_preord]);
        ix_preord++;

        rt->left = self(low, rt->val); // left subtree
        rt->right = self(rt->val, high);

        return rt;
    };

    return tree(buildTree, INT_MIN, INT_MAX); */

	int ix = 0;
	return helper(A, ix, INT_MAX);
}

/*
 *
 * int n, idx = 0;
vector<int> pre;
TreeNode* helper(int lower, int upper) {
    if (idx == n)
        return NULL;
    int val = pre[idx];
    if (val < lower || val > upper)
        return NULL;
    idx++;
    TreeNode* root = new TreeNode(val);
    root->left = helper(lower, val);
    root->right = helper(val, upper);
    return root;
}
TreeNode* Solution::constructBST(vector<int> &A) {
    pre = A;
    n = A.size();
    idx = 0;
    return helper(-2000000000, 2000000000);
}

class Solution:
    def constructBST(self, A):
        def helper(lower = float('-inf'), upper = float('inf')):
            nonlocal idx
            if idx == n:
                return None
            val = A[idx]
            if val < lower or val > upper:
                return None
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        idx = 0
        n = len(A)
        return helper()

GO:
 * type treeNode struct {
 *     left *treeNode
 *     value int
 *     right *treeNode
 * }
 *
 * func treeNode_new(val int) *treeNode{
 *     var node *treeNode = new(treeNode)
 *     node.value=val
 *     node.left=nil
 *     node.right=nil
 *     return node
 * }
 *
 * func constructBST(A []int )  (*treeNode) {
    if len(A) == 0 {
        return nil
    }
    n := treeNode_new(A[0])
    max := 0
    for i := 1 ; i< len(A) ;i++ {
        if A[i] > A[0] {
            max = i
            break
        }
    }
    if max == 0 {
        n.left = constructBST(A[1:len(A)])
        n.right = nil
    } else {
         n.left = constructBST(A[1:max])
         n.right = constructBST(A[max:len(A)])
    }
    return n
}
 *
 */

