# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 18:24:08 2026

@author: USER
"""
'''
Problem Description

Find the Bth smallest element in an unsorted array of non-negative integers A.
Definition of kth smallest element: The kth smallest element is the minimum 
possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then Ak - 1

NOTE: You are not allowed to modify the array (The array is read-only). Try to do it using constant extra space.

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
'''
def kthsmallest(A, B):
    # A.sort()
    # return A[B - 1]
    low = 1
    high = 2147483647
    n_A = len(A)
    
    for i in range(n_A):
        low = min(low, A[i])
        high = max(high, A[i])

    def count(A, x):
        result = 0
        for i in range(n_A):
            if A[i] <= x:
                result += 1
        return result     
 
    while low < high:
        mid = low + (high - low) // 2
        if count(A, mid) < B:
            low = mid + 1
        else:
            high = mid
    return high

    