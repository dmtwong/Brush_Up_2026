# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 13:02:17 2026

@author: USER
"""
'''
Given a number N, verify if N is prime or not.

Return 1 if N is prime, else return 0.

Example :

Input : 7
Output : True
Problem Approach:

VIDEO : https://www.youtube.com/watch?v=7VPA-HjjUmU

Complete code in the hint.
class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, A):

'''

def isPrime(A):
    if A <= 3:
        return True
    upper = round(A ** 0.5) + 1
    for i in range(2, upper + 1):
        if A % i == 0:
            print(i)
            return 0   
    return 1


# A = 84923
# 84923//163
# 163 * 521
# isPrime(A)

'''
int Solution::isPrime(int A) {
    if(A==1) return 0;
    for(int i=2 ; i*i<=A ; i++)
        if(A%i==0) return 0;
    return 1;
}
# Scala
class Solution {
    def isPrime(A: Int): Int  = {
        if (A<2)
            return 0
        val sqrtA = math.sqrt(A).toInt
        for (i <- 2 to sqrtA) {
            if (A%i==0) {
                return 0
            }
        }
        1
    }
}

# GO
import "math"

func isPrime(a int) int {
	if a <= 1 {
		return 0
	}

	for i := 2; i <= int(math.Sqrt(float64(a))); i++ {
		if a % i == 0 && a != i {
			return 0
		}
	}
	return 1
}
'''
