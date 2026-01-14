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

# C++
'''   
vector<int> Solution::sieve(int A) 
{
    int n=A;
    int i,j;
    
    vector<bool>v(n+1);
    vector<int>m;
    for(i=0;i<=n;i++)
        v[i]=true;
    for(i=2;i<=n;i++)
    {
        if(v[i])
        {
            m.push_back(i);
            for(j=2;i*j<=n;j++)
            {
                //if(j!=i)
                    v[i*j]=false;
            }
        }
    }
    //free(v);
    return m;
} 
'''

# Scala
'''
class Solution {
    def sieve(A: Int): Array[Int]  = {
        val s : Array[Int] = Array.fill[Int](A+1)(1);
        val mid = A/2
        for (i <- 2 to mid) {
            var ij = 2 * i
            while (ij <= A) {
                s(ij) = 0
                ij += i
            }
        }
        s.indices.filter(i => s(i)==1).toArray.slice(2, s.length)
    }
}

'''



