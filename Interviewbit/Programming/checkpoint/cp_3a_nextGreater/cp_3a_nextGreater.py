# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 18:17:13 2026

@author: USER
"""
# Given an array, find the next greater element G[i] for every element A[i] in the array.  The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array. 
# More formally,
# G[i] for an element A[i] = an element A[j] such that 
#     j is minimum possible AND 
#     j > i AND
#     A[j] > A[i]
# Elements for which no greater element exist, consider next greater element as -1.
# Example:
# Input : 
A = [4, 5, 2, 10]
# Output : [5, 10, 10, -1]
# Example 2:
# Input : 
A = [3, 2, 1]
# Output : [-1, -1, -1]

# class Solution:
# 	# @param A : list of integers
# 	# @return a list of integers
# 	def nextGreater(self, A):
def nextGreater(A):
    n_A = len(A)
    # result = list()
    result = [-1] * n_A
    for i in range(n_A - 1):
        A_i = A[i]
        for j in range(i + 1, n_A) :
            A_j = A[j]
            if A_i < A_j:
                # print(i, j, 'here')
                result[i] = A_j
                break
            # print(i, j)
        # result[i] = -1
    # result[-1] = -1
    return result
nextGreater(A)
        