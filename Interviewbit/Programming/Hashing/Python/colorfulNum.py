# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 12:25:28 2026

@author: USER
"""

Problem Description
For Given Number A, find if it's a COLORFUL number or not.
COLORFUL number:
A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Return 1 if A is a COLORFUL number, else return 0
Problem Constraints
0 <= A <= 109

Input Format
The first argument is an integer A.


Output Format
Return 1 if A is a COLORFUL number, else return 0


def colorful(n):
    str_A = str(A)
    n_A = len(str_A)
    tbl = dict()    
    for i in range(n_A):
        for j in range(i, n_A):
            sub = str_A[i:j+1]
            p = 1
            for c in sub:
                p *= int(c)
            if p in tbl:
                # print(tbl)
                return 0
            tbl[p] = 1    
    return 1

# A = 23
# A = 233
# A = 2323
# A = 1234234
# colorful(A)


'''
int Solution::colorful(int A) {
   if (A < 10) return 1;
	set<int> s;
	vector<int> v;
	while (A) {
		int lastdigit = A % 10;
	    A /= 10;
		for (auto &i : v) i *= lastdigit;
		v.push_back(lastdigit);
		for (auto i : v) {
			if (s.count(i)) return 0;
			else s.insert(i);
		}
	}
	return 1;
}

# Scala:
    class Solution {
    def colorful(A: Int): Int  = {
    val digits = math.log10(A).toInt + 1
    val set = new collection.mutable.HashSet[Int]

    for (windowSize <- 1 to digits) {
      var num = A
      for (i <- 1 to digits - windowSize + 1) {
        val n = (num % (math.pow(10, windowSize))).toInt
        val res = n.toString.toList.map(_.asDigit).foldLeft(1)(_ * _)
        if (set.contains(res)) return 0
        set += res
        num /= 10
      }
    }

    1
    }
}

/**
 * @input A : Integer
 * 
 * @Output Integer
 */
import (
    "strconv"
)
    
func colorful(A int )  (int) {
        strA := strconv.Itoa(A)
        subNums := []string{}
        for i := 1; i <= len(strA); i++ {
                for j := 0; i+j <= len(strA); j++ {
                        subNums = append(subNums, strA[j:i+j])
                }
        }
        sumMap := map[int]bool{}

        for i := 0; i < len(subNums); i++ {
                prod := 1
                for j := len(subNums[i]) - 1; j >= 0; j-- {
                        digit := int(subNums[i][j] - '0')
                        prod *= digit
                }
                if _, ok := sumMap[prod]; ok {
                        return 0
                }
                sumMap[prod] = true
        }
        return 1
}

'''