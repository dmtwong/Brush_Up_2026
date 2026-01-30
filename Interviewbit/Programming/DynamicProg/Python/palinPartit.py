# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:41:08 2026

@author: mingt
"""

'''
Problem Description
Given a string A, partition A such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of A.
Problem Constraints
1 <= length(A) <= 501
Input Format
The first and the only argument contains the string A.
Output Format
Return an integer, representing the minimum cuts needed.
Example Input
Input 1:
 A = "aba"
Input 2:
 A = "aab"
Example Output
Output 1:
 0
Output 2:
 1
Example Explanation
Explanation 1:
 "aba" is already a palindrome, so no cuts are needed.
Explanation 2:
 Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
def minCut(A):
    n_A = len(A)
    is_pali = [[False] * n_A for i in range(n_A)]
    cnt_cuts = [0] * n_A    
    for i in range(n_A - 1, -1, -1):
        for j in range(i, n_A):
            if A[i] == A[j] and (j - i <= 2 or is_pali[i + 1][j - 1]):
                is_pali[i][j] = True

    for i in range(n_A):
        if is_pali[0][i]:
            cnt_cuts[i] = 0  
            # print('here', i, cnt_cuts)
        else:
            cnt_cuts[i] = i  
            # print('there', i, cnt_cuts)
            for j in range(1, i + 1):
                if is_pali[j][i]:
                    # print('!!!', i, j, cnt_cuts[i])
                    cnt_cuts[i] = min(cnt_cuts[i], cnt_cuts[j - 1] + 1)
                    # print(cnt_cuts[i])
    return cnt_cuts[-1]
# A = 'abba'
# A = 'abbaba'
# A = 'aabbaaa'
# A = 'aabbbbb'
# A = 'abcdefg'
# minCut(A)


''' Editorial:
import sys
from functools import lru_cache
sys.setrecursionlimit(100000)
class Solution:
    # @param A : string
    # @return an integer
    @lru_cache(100000)
    def minCut(self, s):
        return 0 if s[::-1] == s else min(1 + self.minCut(s[i:]) for i in range(1, len(s)) if s[:i][::-1] == s[:i])
C++
int Solution::minCut(string A) {
    int n=A.size();
    int dp[n],palin[n][n];
    memset(palin,0,sizeof palin);
    for(int i=1;i<=n;i++)
    {
        for(int j=0;j<n;j++)
        {
            int l=j,r=j+i-1;
            if(i==1) palin[l][l]=1;
            else if(i==2 && j+1<n) palin[l][r]=(A[l]==A[r]);
            else if(r<n)
            {
                if(palin[l+1][r-1] && A[l]==A[r])
                {
                    palin[l][r]=1;
                }
            }
        }
    }
    for(int i=0;i<n;i++) dp[i]=INT_MAX;
    for(int i=0;i<n;i++)
    {
        for(int j=i;j<n;j++)
        {
            if(i==0)
            {
                if(palin[i][j]) dp[j]=0;
            }
            else
            {
                if(palin[i][j])
                {
                    dp[j]=min(dp[j],dp[i-1]+1);
                }
            }
        }
    }
    return dp[n-1];
}            
 # Scala:
class Solution {
  def minCut(s: String): Int  = {
    val n = s.length
    val c = Array.ofDim[Int](n)
    val p = Array.ofDim[Boolean](n, n)
    
    for (i <- 0 until n) p(i)(i) = true
    
    for (l <- 2 to n) {
      for (i <- 0 until n - l +1) {
        val j = i + l - 1
        if (l == 2) p(i)(j) = s(i) == s(j)
        else p(i)(j) = s(i) == s(j) && p(i+ 1)(j - 1)
      }
    }
    
    for (i <- 0 until n) {
      if (p(0)(i)) c(i) = 0
      else {
        c(i) = Integer.MAX_VALUE
        for (j <- 0 until i) {
          if (p(j + 1)(i) && 1 + c(j) < c(i)) {
            c(i) = 1 + c(j)
          }
        }
      }
    }
    c(n - 1)
  }
}

# GO:
    func minCut(A string) int {

	rA := make([]rune, 0, len(A))
	for _, r := range A {
		rA = append(rA, r)
	}

	DP := minCutDP(rA)
	return DP[len(rA)-1]
}

func minCutDP(A []rune) []int {
	N := len(A)
	pDP := getIsPalindromeDP(A)
	DP := make([]int, len(A))

	for i := 0; i < N; i++ {
		if pDP[0][i] == 1 {
			DP[i] = 0
		} else {
			for j := 0; j < i; j++ {
				if pDP[j+1][i] == 1 {
					if DP[j] <= DP[i-1] {
						DP[i] = DP[j] + 1
					} else {
						DP[i] = DP[i-1] + 1
					}
					break
				}
			}
		}

	}

	return DP
}

func getIsPalindromeDP(A []rune) [][]int {
	N := len(A)
	DP := make([][]int, N)
	for i := range DP {
		DP[i] = make([]int, N)
	}

	for slice := 1; slice <= N; slice++ {
		for i := 0; i+slice <= N; i++ {
			j := i + slice - 1
			if slice == 1 {
				DP[i][i] = 1
			} else if slice == 2 {
				if A[i] == A[j] {
					DP[i][j] = 1
				}
			} else {
				if A[i] == A[j] && DP[i+1][j-1] == 1 {
					DP[i][j] = 1
				}
			}
		}
	}
	return DP
}
'''

