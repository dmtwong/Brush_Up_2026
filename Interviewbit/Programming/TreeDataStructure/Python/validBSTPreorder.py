# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 15:02:40 2026

@author: mingt
"""

'''
Problem Description
You are given a preorder traversal A, of a Binary Search Tree.
Find if it is a valid preorder traversal of a BST.
Note: Binary Search Tree by definition has distinct keys and duplicates in binary search tree are not allowed.
Problem Constraints
1 <= A[i] <= 106
1 <= |A| <= 105

Input Format
First and only argument is an integer array A denoting the pre-order traversal.

Output Format
Return an integer:
0 : Impossible preorder traversal of a BST
1 : Possible preorder traversal of a BST

Example Input
Input 1:
A = [7, 7, 10, 10, 9, 5, 2, 8]

Example Output
Output 1:
 0
 class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

 
'''
def solve(A):
    def isValid(A, low, up):       
        if low >= up:
            return 1
        root = A[low]
        i = low
        while i < up:
            if A[i] > root:
                break
            i += 1
        
        j = i
        while j < up:
            if A[j] < root:
                return 0
            j += 1
        isVal = isValid(A, low + 1, i) and isValid(A, i, up)
        return isVal        
    n_A = len(A)
    stack = {}
    for i in A:
        try:
            stack[i]
            return 0
        except:
            stack[i] = 1
    return isValid(A, 0, n_A)
solve(A)


'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A)!=len(list(set(A))) or max(A)!=A[-1]:

            return 0

        return 1

C++

bool canRepresentBST(vector<int>& pre, int n) 
{ 
    // Create an empty stack 
    stack<int> s; 
  
    // Initialize current root as minimum possible 
    // value 
    int root = INT_MIN; 
  
    // Traverse given array 
    for (int i=0; i<n; i++) 
    { 
        // If we find a node who is on right side 
        // and smaller than root, return false 
        if (pre[i] < root) 
            return false; 
  
        // If pre[i] is in right subtree of stack top, 
        // Keep removing items smaller than pre[i] 
        // and make the last removed item as new 
        // root. 
        while (!s.empty() && s.top()<pre[i]) 
        { 
            root = s.top(); 
            s.pop(); 
        } 
  
        // At this point either stack is empty or 
        // pre[i] is smaller than root, push pre[i] 
        s.push(pre[i]); 
    } 
    return true; 
} 
int Solution::solve(vector<int> &A) {
    assert(A.size()>=1 && A.size()<=100000);
    set<int>s;
    for(int a:A){
        assert(a>=1 && a<=1000000);
        s.insert(a);
    }
    if(s.size() != A.size()){
        return 0;
    }
    if(canRepresentBST(A,A.size()))
        return 1;
    return 0;
}
Scala:
class Solution {
    def solve(pre: Array[Int]): Int  = {
        val n=pre.length
        val s = scala.collection.mutable.Stack[Int]()
        var root = Int.MinValue   
        
        for (i <- 0 until n) {             
            if (pre(i) < root) return 0                            
            while (!s.isEmpty && s.top < pre(i)) root = s.pop()                                    
            s.push(pre(i))
        } 
        return 1
    }
}

GO:
 import "math"

/**
 * @input A : Integer array
 * 
 * @Output Integer
 */
func solve(A []int) int {
    s := []int{}
    root := math.MinInt32
    l := len(A)
    for i := 0; i < l; i++ {
        if A[i] < root {
            return 0
        }
        for len(s) != 0 && s[len(s)-1] < A[i] {
            root = s[len(s)-1]
            s = s[:len(s)-1]
        }
        s = append(s, A[i])
    }
    return 1
}   
'''
