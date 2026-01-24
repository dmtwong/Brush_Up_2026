# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 12:51:44 2026

@author: USER
"""

'''
Problem Description
Given an 1D integer array A containing N distinct integers.
Find the number of unique pairs of integers in the array whose XOR is equal to B.
NOTE:
Pair (a, b) and (b, a) is considered to be same and should be counted once.
Problem Constraints
1 <= N <= 105
1 <= A[i], B <= 107

Input Format
First argument is an 1D integer array A.
Second argument is an integer B.

Output Format
Return a single integer denoting the number of unique pairs of integers in the array A whose XOR is equal to B.

Example Input
Input 1:
 A = [5, 4, 10, 15, 7, 6]
 B = 5
Input 2:
 A = [3, 6, 8, 10, 15, 50]
 B = 5
Example Output
Output 1:
 1
Output 2:
 2
Example Explanation
Explanation 1:
 (10 ^ 15) = 5
Explanation 2:
 (3 ^ 6) = 5 and (10 ^ 15) = 5 
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n_A = len(A)
        for i in 
'''
def solve(A, B):
    # n_A = len(A)
    # count = 0
    # dictionary_i = {}
    # # dictionary_j = {}
    # for i in range(n_A - 1):
    #     a = A[i]
    #     # print(a)
    #     if a in dictionary_i:
    #         # print(a, ' skipped')
    #         continue        
    #     for j in range(i, n_A):            
    #         b = A[j]
    #         # print(a, b)
    #         if a ^ b == B:
    #             # print(a, b, count)
    #             count += 1
    #             dictionary_i[a] = 1
    #             dictionary_i[b] = 1
    #             continue
    # return count
    n_A = len(A)
    result = 0
    s = set()
    for i in range(0, n_A):
        if(B ^ A[i] in s):
            result = result + 1
        s.add(A[i])
    return result

        
solve(A, B)     
