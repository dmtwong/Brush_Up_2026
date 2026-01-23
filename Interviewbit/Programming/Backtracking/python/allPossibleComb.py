# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 20:16:49 2026

@author: USER
"""

'''
Problem Description
You are given a array of strings A of length N.
You have to return another string array which contains all possible special strings in Lexicographic order.
 A special string is defined as a string with length equal to N, 
 and ith character of the string is equal to any character of the ith string in the array A.

Problem Constraints
1 <= N <= 5
1 <= |Ai| <= 8

Input Format
The first argument is the string array A.
Output Format
Return a string array consisting of all possible special strings.
Example Input
Input 1:
A = ['ab', 'cd']
Input 2:
A = ['aa', 'bb']
Example Output
Output 1:
['ac', 'ad', 'bc', 'bd']
Output 2:

['ab', 'ab', 'ab', 'ab']
Example Explanation
Explanation 1:
Since, the first character has to be from the 1st string 'ab' and the 2nd from 'cd'.
These are the all possible 4 combinations.
Explanation 2:
Note we can have duplicate strings, you have to add all of them.

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def specialStrings(self, A):
'''
from itertools import product
def specialStrings(A):
    n_A = len(A)
    if n_A == 0:
        return A
    elif n_A == 1:
        return [i for i in A[0]]
    result = A[0]
    for i in range(1, n_A):
        a = result
        b = A[i]
        result = list(product(a, b))
        print(a, b, result)
        result = [''.join(i) for i in result]
        print(result)
    print(result)
    return result
# A = [ "qyzn" ]
# A = [ "ozqz", "p", "abm" ] # opa opb opm qpa qpb qpm zpa zpa zpb zpb zpm zpm 

# specialStrings(A)

'''
class Solution:
    # @param A : list of strings
    # @return a list of strings
    def specialStrings(self, a):
        def comb(a):
            if not a:
                return ['']
            
            return [
                e + s 
                for e in a[0]
                for s in comb(a[1:])]
                
        return comb(a)
# C++
vector < string > ans;
void rec(vector < string > & A, int i, int j, string par) {
    string curr = par;
    if (i == A.size()) {
        ans.push_back(curr);
        return;
    }
    if (j < A[i].length() - 1) {
        rec(A, i, j + 1, curr);
    }
    curr += A[i][j];
    rec(A, i + 1, 0, curr);
}

vector < string > Solution::specialStrings(vector < string > & A) {
    ans.clear();
    string curr = "";
    rec(A, 0, 0, curr);
    
     
    return ans2;
}

# GO
/**
 * @input A : array of strings
 * 
 * @Output string array.
 */
 
import (
    "strings"
    "sort"
)
func specialStrings(A []string) []string {
    ans := []string{}
    if len(A) == 0 {
        return ans
    }
    c := []string{}
    d := &c
    first := strings.Split(A[0], "")
    for _, a := range first {
        combine(a, A[1:], d)
    }
    sort.Strings(c)
    return c
}

func combine(a string, b []string, c *[]string) {
    if len(b) == 0 {
        *c = append(*c, a)
    } else {
        temp := b[0]
        b = b[1:]
        tempArr := strings.Split(temp, "")
        for _, s := range tempArr {
            combine(a+s, b, c)
        }
    }
}
'''