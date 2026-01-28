//============================================================================
// Name        : nextPointerBinaryTree.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

/*
 Given a binary tree
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example :

Given the following perfect binary tree,

         1
       /  \
      2    5
     / \  / \
    3  4  6  7
After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 5 -> NULL
     / \  / \
    3->4->6->7 -> NULL
Note that using recursion has memory overhead and does not qualify for constant space.
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}

*/

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct TreeLinkNode {
  int val;
  TreeLinkNode *left, *right, *next;
  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
};

//void Solution::connect(TreeLinkNode* A) {
void connect(TreeLinkNode* A) {
    TreeLinkNode* prev;
    int n_tree, i;
    queue<TreeLinkNode*> tree;
    tree.push(A);
    while (tree.size() > 0){
    	n_tree = tree.size();
        prev = NULL;
        for (i = 0; i < n_tree; i++){
            TreeLinkNode* cur = tree.front();
            tree.pop();

            if (prev == NULL){
                prev = cur;
            } else {
                prev->next = cur;
                prev = cur;
            }
            if (cur->left){
                tree.push(cur->left);
            }
            if (cur->right){
                tree.push(cur->right);
            }
        }
        prev->next = NULL;
    }
}

/*
void Solution::connect(TreeLinkNode* root) {
    if(!root)return;
    if(!root->left && !root->right)return;

    queue<TreeLinkNode*> q;
    q.push(root);
    while(!q.empty()){
        TreeLinkNode *parent=q.front();
        q.pop();

        if(parent->left && parent->right){
            TreeLinkNode *leftchild=parent->left;
            TreeLinkNode *rightchild=parent->right;
            leftchild->next=rightchild;

            TreeLinkNode *parent_siblling=parent->next;
            if(parent_siblling)
            rightchild->next=parent_siblling->left;

            q.push(parent->left);
            q.push(parent->right);
        }

    }

}

///////////////////////////
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        dummy=tail=TreeLinkNode(0)
        while root and root.left:
            tail.next=root.left
            tail=tail.next
            tail.next=root.right
            tail=tail.next
            root=root.next
            if not root:
                tail=dummy
                root=dummy.next

////////////////////////////
void Solution::connect(TreeLinkNode* root) {
    queue<TreeLinkNode* > q;
    q.push(root);
     while(!q.empty()){
         int n = q.size();
         for(int i = 0;i<n;i++){
             TreeLinkNode* curr = q.front();
             q.pop();
             if(i==n-1)curr->next = NULL;
             else{
                 TreeLinkNode* temp = q.front();
                 curr->next = temp;
             }
             if(curr->left)q.push(curr->left);
             if(curr->right)q.push(curr->right);
         }  }
     return ;
}

/////////////////////////////
void Solution::connect(TreeLinkNode* A) {
	for (TreeLinkNode* S = A; S->left; S = S->left) { // traverse to (left) child
		for (TreeLinkNode* C = S; C; C = C->next) { // traverse to siblings
			C->left->next = C->right;
			if (C->next) C->right->next = C->next->left;
		}
	}
}
 */
