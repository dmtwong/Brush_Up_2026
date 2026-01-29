# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:18:00 2026

@author: mingt
"""

'''
Problem Description
Given two strings A and B. Find the longest common sequence ( A sequence which does not need to be contiguous), which is common in both the strings.
You need to return the length of such longest common subsequence.
Problem Constraints
1 <= |A|, |B| <= 1005
Input Format
First argument is an string A.
Second argument is an string B.
Output Format
Return the length of such longest common subsequence between string A and string B.
Example Input
Input 1:
 A = "abbcdgf"
 B = "bbadcgf"
Example Output
Output 1:
 5
 class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):

'''

# { a:1, b:2, c:1, d:1, g:1, f:1}`

def solve(A, B):
    n_A = len(A)
    n_B = len(B)
    r_A = [0] * (n_A + 1)
    grid = []
    for i in range(n_B + 1):
        grid.append(r_A[:])
    # print(grid)
    for i in range(n_A):
        for j in range(n_B):
            if A[i] == B[j]:
                # print(i, A[i], grid[i][j])
                grid[i + 1][j + 1] = grid[i][j] + 1
            else:
                nextB = grid[i][j + 1]
                nextA = grid[i+1][j]
                # print(i, j, A[i], B[j]) #, grid[i, j + 1], grid[i+ 1, j], nextA, nextB)
                grid[i + 1][j + 1] = max(nextA, nextB)
    return grid[n_A][n_B]

solve(A,B)
'''
int Solution::solve(string A, string B) {
   int m = A.size(), n = B.size();
   int L[m+1][n+1]; 
   int i, j; 
   
   for (i=0; i<=m; i++) 
   { 
     for (j=0; j<=n; j++) 
     { 
       if (i == 0 || j == 0) 
         L[i][j] = 0; 
   
       else if (A[i-1] == B[j-1]) 
         L[i][j] = L[i-1][j-1] + 1; 
   
       else
         L[i][j] = max(L[i-1][j], L[i][j-1]); 
     } 
   } 
     
   return L[m][n]; 
}
# Scala:
    import scala.collection.mutable
import scala.math
class Solution {

    val mp = mutable.Map[String, Int]()

    def helper(A: String, B: String, m: Int, n: Int): Int = {
        if (m == 0 || n == 0) return 0
        
        if (mp.contains(m.toString + n.toString)) {
            return mp(m.toString + n.toString)
        }
        
        val ans = if (A(m) == B(n)) {
            1 + helper(A, B, m-1, n-1)
        } else {
            math.max(helper(A, B, m-1, n),
                helper(A, B, m, n-1))
        }
        mp(m.toString + n.toString) = ans
        ans
    }
    
    def solve(A: String, B: String): Int  = {
        val arr = Array.ofDim[Int](A.size+1, B.size+1)
        
        for (i <- 0 to A.size) {
            for (j <- 0 to B.size) {
                if (i == 0 || j == 0) {
                    arr(i)(j) = 0
                } else if (A(i-1) == B(j-1)) {
                    arr(i)(j) = 1 + arr(i-1)(j-1)
                } else {
                    arr(i)(j) = math.max(arr(i)(j-1),
                        arr(i-1)(j))
                }
            }
        }
        arr(A.size)(B.size)
        //helper(A, B, A.size-1, B.size-1)
    }
}
GO:
    /**
 * @input A : String
 * @input B : String
 * 
 * @Output Integer
 */
func solve(A string , B string )  (int) {
    if len(A) == 0 || len(B) == 0 {
        return 0
    }
    cache := make([][]int, len(A))
    for i := 0; i < len(A); i++ {
        cache[i] = make([]int, len(B))
    }
    
    for i :=0; i < len(A); i++ {
        for j := 0; j < len(B); j++ {
            cache[i][j] = -1
        }
    }
    
    return findCommonCount(A, B, 0, 0, cache)
}

func findCommonCount(A, B string, i, j int, cache [][]int) int {
    if i >= len(A) {
        return 0
    }
    if j >= len(B) {
        return 0
    }
    if v := cache[i][j]; v != -1 {
        return v
    }
    
    first := findCommonCount(A, B, i + 1, j + 1, cache)
    if A[i] == B[j] {
        first +=1
    }
    second := findCommonCount(A, B, i + 1, j, cache)
    third := findCommonCount(A, B, i, j+1, cache)
    
    result := first
    if result < second {
        result =second
    }
    if result < third {
        result =third
    }
    
    cache[i][j] = result
    return result
    
}
'''