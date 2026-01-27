//============================================================================
// Name        : rtViewBinaryTree.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;
/*
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}

*/

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


vector<int> res;
void helper(TreeNode* A, int ix){
    if (A == NULL){
        return;
    }
    if (res.size() == ix){
        res.push_back(A->val);
    }
    helper(A->right, ix + 1);
    helper(A->left, ix+1);
}
//vector<int> Solution::solve(TreeNode* A) {
vector<int> solve(TreeNode* A) {
    res.clear();
    helper(A, 0);
    return res;
}


/*
 *
 *  vector<int> rightview(TreeNode *root){
    vector<int> ans;
    queue< TreeNode * , int > q;  // which stores the Node and its level
    bool lev[100000];
    memset(lev,false,sizeof lev); // initialising the lev array to false
    if(root==NULL)
        return ans;
    q.push(root);
    q.push(NULL);
    while(!q.empty()){
        TreeNode *temp=q.front();
        if(temp){
            ans.push_back(temp->val);
            while(q.front()!=NULL){
                if(temp->right)
                    q.push(temp->right);
                if(temp->left)
                    q.push(temp->left);
                q.pop();
                temp=q.front();
            }
            q.push(NULL);
        }
    q.pop();
    }
return ans;
}
vector<int> Solution::solve(TreeNode* A) {
    return rightview(A);
}

def printRightView(root):
    ans=[]
    if (not root):
        return
    q = []
    q.append(root)
    while (len(q)):
        # number of nodes at current level
        n = len(q)
        # Traverse all nodes of current level
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
            # Print the right most element
            # at the level
            if (i == n) :
                ans.append(temp.val)
            # Add left node to queue
            if (temp.left != None) :
                q.append(temp.left)
            # Add right node to queue
            if (temp.right != None) :
                q.append(temp.right)
    return ans
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        return printRightView(A)

Scala:
module.exports = {
 //param A : root node of tree
 //return a array of integers
	solve : function(A){

	    var set_ = {};
	    var ans = [];

	    function recur(A,lev){
	        if(A == null)
	            return;

	        if(!(set_[lev]==true)){
	            set_[lev] = true;
	            ans.push(A.data);
	        }

	        recur(A.right,lev+1);
	        recur(A.left,lev+1);
	        return;
	    }

	    recur(A,0);
        return ans;
	}
};
 */
