# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 22:55:22 2026

@author: USER
"""
'''
Problem Description
Given a matrix of integers A of size N x M in which each row is sorted.
Find and return the overall median of matrix A.
NOTE: No extra memory is allowed.
NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.
Problem Constraints
1 <= N, M <= 10^5
1 <= N*M <= 10^6
1 <= A[i] <= 10^9
N*M is odd
Input Format
The first and only argument given is the integer matrix A.
Output Format
Return the overall median of matrix A.
Example Input
Input 1: 
A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ] 
Input 2: 
A = [   [5, 17, 100]    ]
Example Output
Output 1: 
 5 
Output 2: 
 17
Example Explanation
Explanation 1: 
A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5. 
Explanation 2:
Median is 17.
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def findMedian(self, A):

'''
def findMedian(A):
    A_2 = []
    n_row, n_col = len(A), len(A[0])
    for i in range(n_row):
        for j in range(n_col):
             A_2.append(A[i][j])
    A_2.sort() 
    mid = len(A_2) // 2 
    if n_row % 2 == 0: 
        return (A_2[mid-1] + A_2[mid]) / 2 
    else: 
        return A_2[mid] 

