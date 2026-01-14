# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 20:15:39 2026

@author: USER
"""

"""
Problem Description
Given a number A, find all prime numbers up to A (A included).
Make sure the returned array is sorted.

Problem Constraints
1 <= A <= 106
Input Format
The first argument is an integer A.

Output Format
Return array of integers.
Example Input
A = 7
Example Output
[2, 3, 5, 7]

Example Explanation
All primes till 7 are, 2, 3, 5 and 7
class Solution:
	# @param A : integer
	# @return a list of integers
	def sieve(self, A):
"""
def sieve(A):
    ans = []
    if A < 2:
        return ans
    # elif A == 2:
    #     return [2]
    else:
        # ans.append(2)
        for i in range(2, A + 1):
            # ans.append(i)
            isPrime = True
            for j in range(2, int(i ** 0.5 ) + 1):
                if i % j == 0:
                    isPrime = False
                    break
                    # print(i, j)
                    # ans.pop()
            if isPrime == True:
                ans.append(i)
    return ans

# for k in range(2, 12):
#     print(sieve(k))

