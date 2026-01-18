# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 19:14:27 2026

@author: USER
"""

'''
Given an array of non negative integers A, and a range (B, C), 
find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C
Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]
where 0 <= i <= j < size(A)
Example :
A : [10, 5, 1, 0, 2]
(B, C) : (6, 8)
ans = 3 
as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in the range [6, 8]
NOTE : The answer is guranteed to fit in a 32 bit signed integer.
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return an integer
	def numRange(self, A, B, C):

'''
def numRange(A, B, C):
    def cnt(A, x):
        n_A = len(A)
        lo, up, r_sum, numSub = 0, 0, 0, 0        
        while up < n_A :       
            # print(x, r_sum, lo, A[lo], up, A[up], numSub)
            r_sum += A[up] 
            while (lo <= up and r_sum > x) :
                # print('here', lo, up, r_sum, x)
                r_sum -= A[lo]
                lo += 1
            # print('there', up, lo)
            numSub += (up - lo + 1)
            up += 1     
        return numSub    
    lf_C = cnt(A, B - 1) 
    rt_C = cnt(A, C)
    return rt_C - lf_C


