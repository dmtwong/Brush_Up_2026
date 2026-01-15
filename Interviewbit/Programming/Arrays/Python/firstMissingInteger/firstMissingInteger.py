# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 22:27:20 2026

@author: USER
"""

"""
Problem Description

Given an unsorted integer array, find the first missing positive integer.
Your algorithm should run in O(n) time and use constant space.
Problem Constraints
1 <= |A| <= 106
-106 <= Ai <= 106
Input Format
The first argument is an integer array A.
Output Format
Return an integer equal to the first missing positive integer
Example Input
Input 1:
A = [1,2,0]
Input 2:
A = [3,4,-1,1]
Input 3:
A = [-8,-7,-6]
Example Output
Output 1:
3
Output 2:
2
Output 3:
1
Example Explanation
Explanation 1:
3 is the first positive missing integer.
Explanation 2:
2 is the first positive missing integer.
Explanation 3:
1 is the first positive missing integer.

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):

"""

def firstMissingPositive(A):
    n_A = len(A)
    ix_list = [False] * n_A
    for i in A:        
        if i >= 1 and i <= n_A:
            # print(i)
            ix_list[i-1] = True
    for j in range(n_A):
        if ix_list[j] == False:
            # print('here')
            return j + 1
    # print('there', j)
    return j + 2

# scala
'''
class Solution {
    def firstMissingPositive(A: Array[Int]): Int  = {
      val len = A.length
      val buff = Array.ofDim[Int](len)
      A.foreach(ai => if (ai > 0 && ai <= len) buff(ai - 1) = buff(ai - 1) + 1)
    
      for {
        i <- buff.indices
        ai = buff(i)
        if ai == 0
      } return i + 1
      len + 1
    }
}

'''

# c++
''' 
int Solution::firstMissingPositive(vector<int> &A) {
    int n = A.size();
    for (int i = 0; i < n; i++) {
        if (A[i] > 0 && A[i] <= n) {
            int pos = A[i] - 1;
            if (A[pos] != A[i]) {
                swap(A[pos], A[i]);
                i--;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        if (A[i] != i + 1) return (i + 1);
    }
    return n + 1;
}
'''

# GO
'''
/**
 * @input A : Integer array
 * 
 * @Output Integer
 */
//Solution based on slight variation of pegionhole principle, all operations in place. Constant memory used.
func firstMissingPositive(A []int) int {
    //removed all zeroes from array
    for i, el := range A {
        if el == 0 {
            A[i] = -1
        }
    }
    l := len(A)
    //making all the elements in the array 0 wherever possible
    for _, el := range A {
        for el <= l && el > 0 {
            temp := A[el-1]
            A[el-1] = 0
            el = temp
        }
    }
    //checking where element is not equal to 0 and returning coprresponding value
    for i, el := range A {
        if el != 0 {
            return i + 1
        }
    }
    //if all the elements in the array have become 0, the this is the least positive number missing
    return l + 1
}

'''