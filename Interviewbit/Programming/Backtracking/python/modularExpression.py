# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 16:43:04 2026

@author: USER
"""

'''
Problem Description
Implement pow(A, B) % C.
In other words, given A, B and C, find (AB)%C. 
Problem Constraints
-106 <= A <= 109
0 <= B <= 109
0 <= C <= 109
Input Format
The first argument is an integer A.
The second argument is an integer B.
The third argument is an integer C.
Output Format
Return an integer equal to (AB) % C
Example Input
A = 2, B = 3, C = 3
Example Output
2
Example Explanation
2^3 % 3 = 8 % 3 = 2
class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @return an integer
	def Mod(self, A, B, C):
'''
# A = 2
# B = 3
# C = 3
# Mod(A, B, C)
def Mod(A, B, C):
    if C == 1:
        return 0
    
    ans = 1
    resid = A % C
    # print(B, resid, ans)
    while B > 0:
        if B % 2 == 1:
            ans = (ans * resid) % C        
            # print('here', ans, resid)
        B = B // 2
        resid = (resid ** 2) % C
        # print('there', B, resid, ans)
    # print(A, B, C, ans, resid)
    return ans

'''
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):

        # recursion base case
        if B == 0:
            return 1 % C
        
        # if power is even    
        if B % 2 == 0:
            y = self.Mod(A, B / 2, C)
            return y * y % C
        
        # if power is odd    
        else:
            return (A * self.Mod(A, B - 1, C)) % C
        
int Solution::Mod(int A, int B, int C) {
    A=(A%C+C)%C;
    if(B==0) return 1%C;
    if(B%2)
    return ((long long int)(A%C)*Mod(((long long int)A*A)%C,B/2,C)%C)%C;
    //even
    return Mod(((long long int)A*A)%C,B/2,C)%C;
}

Scala:
class Solution {
  def Mod(a: Int, b: Int, c: Int): Int  = {
    def loop(ma: Long, rb: Int, acc: Long): Long = {
      if (rb == 0) acc
      else loop((ma * ma) % c, rb >> 1, if (rb % 2 == 1) (acc * ma) % c else acc)
    }
    if (a == 0) 0
    else {
      val calc = loop(a.toLong % c, b, 1L).toInt
      if (calc < 0) c + calc else calc
    }
  }
}

GO:
func Mod(A int , B int , C int )  (int) {
    if A==0 {
        return 0
    }
    if B==0 {
        return 1
    }
    for A<0 {
        A+=C
    }
    tmp:=Mod(A, B/2, C)
    tmp=(tmp*tmp)%C
    if B%2==1 {
        return (tmp*(A%C))%C
    }
    return tmp
}

'''
