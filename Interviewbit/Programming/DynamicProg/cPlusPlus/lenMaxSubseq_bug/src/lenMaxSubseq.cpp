//============================================================================
// Name        : lenMaxSubseq.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


/*
NOTE: wrong; review using editorial solution instead: https://www.interviewbit.com/problems/length-of-longest-subsequence/hints/

Problem Description
Given a 1D integer array A of length N, find the length of the longest subsequence which is first increasing (strictly) and then decreasing (strictly).
Problem Constraints
0 <= N <= 3000
 -107 <= A[i] <= 107
Input Format
The first and the only argument contains an integer array A.
Output Format
Return an integer representing the answer as described in the problem statement.
Example Input
Input 1:
 A = [1, 2, 1]
Input 2:
 A = [1, 11, 2, 10, 4, 5, 2, 1]
Example Output
Output 1:
 3
Output 2:
 6
Example Explanation
Explanation 1:
 [1, 2, 1] is the longest subsequence.
Explanation 2:
 [1 2 10 4 2 1] is the longest subsequence.
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
*/

//int Solution::longestSubsequenceLength(const vector<int> &A) {
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
using namespace std;
int longestSubsequenceLength(const vector<int> &A) {
	int n_A = A.size();
	if (n_A < 1){
		return n_A;
	}
	int a_i = A[0];
	int a_next = A[1];
	bool wasUp = a_next > a_i;
	bool isUp;
	int up_max = 0, up_cur = 0, dw_max = 0, dw_cur = 0;
	if (wasUp){
		up_max = 1;
		up_cur = 1;
	//} else {
	}

	for (int i = 2; i < n_A - 2; i++){
		a_i = A[i - 1];
		a_next = A[i];
		isUp = a_i < a_next;
		if (wasUp){
			if (isUp){
				up_cur += 1;
				if (up_max < up_cur){
					up_max = up_cur;
				}
				continue;
			} else {
				wasUp = false;
				up_cur = 0;
				dw_cur += 1;
				continue;
			}
		} else {
			if (!wasUp){
				if (up_max == 0){
					continue;
				}
				dw_cur += 1;
				if (dw_max < dw_cur){
					dw_max = dw_cur;
				}
				continue;
			} else {
				wasUp = true;
				up_cur += 1;
				dw_cur = 0;
			}
		}
	}
	return up_max + dw_max;
}

/*
Editorial:
int Solution::longestSubsequenceLength(const vector<int> &A) {
	int n = A.size();
	assert(n>=0 && n<=3000);
	for(int a:A)
	    assert(a>=-10000000 && a<=10000000);
	int inc[n];
	int dec[n];
	int ct = 0;

	inc[0] = 1;
	for(int i=1; i<n; i++)
	{
		inc[i] = 1;
		for(int j=i-1; j>=0; j--)
		{
			if(A[i] > A[j] && inc[i] < inc[j] + 1)
				inc[i] = inc[j] + 1;
		}
	}

	dec[n-1] = 1;
	for(int i=n-2; i>=0; i--)
	{
		dec[i] = 1;
		for(int j=i+1; j<n; j++)
		{
			if(A[i] > A[j] && dec[i] < dec[j] + 1)
				dec[i] = dec[j] + 1;
		}
	}

	int mx = 0;
	for(int i=0; i<n; i++)
		mx = max(mx, inc[i] + dec[i] - 1);

	return mx;
}

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        n=len(A)
        inc=[1]*n
        for i in range(1,n):
            for j in range(0,i):
                if A[i]>A[j] and inc[j]+1>inc[i]:
                    inc[i]=inc[j]+1

        dec=[1]*n
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if A[i]>A[j] and dec[j]+1>dec[i]:
                    dec[i]=dec[j]+1
        maximum=1
        for x,y in zip(inc,dec):
            maximum=max(maximum,x+y)
        return maximum-1


class Solution {
    def longestSubsequenceLength(A: Array[Int]): Int  = {
      val len = A.length
      if (len == 0) 0
      else {
        val lis = Array.fill[Int](len)(1)
        for {
          i <- 1 until len
          j <- 0 until i
          if A(i) > A(j) && lis(i) < lis(j) + 1
        } lis(i) = lis(j) + 1

        val lds = Array.fill[Int](A.length)(1)
        for {
          i <- len - 2 to 0 by -1
          j <- len - 1 until i by -1
          if A(i) > A(j) && lds(i) < lds(j) + 1
        } lds(i) = lds(j) + 1

        var max = lis(0) + lds(0) - 1
        for {
          i <- 1 until len
          if lis(i) + lds(i) - 1 > max
        } max = lis(i) + lds(i) - 1

        max
      }
    }
}
GO:
func longestSubsequenceLength(A []int) int {
	N := len(A)

	if N <= 1 {
		return N
	}

	ascDP := getAscDP(A)
	descDP := getDescDP(A)

	maxSub := 1

	for i := 0; i < N-1; i++ {
		for j := i + 1; j < N; j++ {
			if A[i] != A[j] {
				sub := ascDP[i] + descDP[j]
				if sub > maxSub {
					maxSub = sub
				}
			}
		}
	}

	return maxSub
}

func getAscDP(A []int) []int {
	N := len(A)

	ascDP := make([]int, N)
	ascDP[0] = 1

	for i := 1; i < N; i++ {
		maxSub := 1
		for j := i; j > 0; j-- {
			if A[i] > A[j-1] {
				sub := ascDP[j-1] + 1
				if sub > maxSub {
					maxSub = sub
				}
			}
		}
		ascDP[i] = maxSub
	}

	return ascDP
}

func getDescDP(A []int) []int {
	N := len(A)

	descDP := make([]int, N)
	descDP[N-1] = 1

	for i := N - 2; i >= 0; i-- {
		maxSub := 1
		for j := i; j < N-1; j++ {
			if A[i] > A[j+1] {
				sub := descDP[j+1] + 1
				if sub > maxSub {
					maxSub = sub
				}
			}
		}
		descDP[i] = maxSub
	}

	return descDP
}
 */
