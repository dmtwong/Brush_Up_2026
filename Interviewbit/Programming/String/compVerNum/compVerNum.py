# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 15:43:36 2026

@author: USER
"""
'''
Problem Description
 
Compare two version numbers version1 and version2.
If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences. For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Note: Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 1.13 < 1.13.4


Problem Constraints
1 <= |A|, |B| <= 5000
class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def compareVersion(self, A, B):
'''
def compareVersion(A, B):
    list_A = A.split('.')
    list_B = B.split('.')
    n_A = len(list_A)
    n_B = len(list_B)
    n = min(n_A, n_B)
    j = abs(n_A - n_B)
    
    for i in range(n):
        A_i = int(list_A[i])
        B_i = int(list_B[i])
        if A_i > B_i:
            return 1
        elif A_i < B_i:
            return -1
        
    if n_A > n_B:
        k = 0
        while j > k: 
            if int(list_A[n + k]) == 0:
                k += 1
                continue
            else:
                return 1
        return 0

    if n_A < n_B:
        k = 0
        while j > k: 
            if int(list_B[n + k]) == 0:
                k += 1
                continue
            else:
                return -1
        return 0
    return 0

# Editorial:
# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return an integer
#     def compareVersion(self, A, B):
#         a=list(map(int,A.split('.')))
#         x=len(a)
#         b=list(map(int,B.split('.')))
#         y=len(b)
#         while(x>y):
#             b.append(0)
#             y+=1
#         while(y>x):
#             a.append(0)
#             x+=1
#         if a>b:
#             return 1
#         if a<b:
#             return -1
#         return 0

# Scala
# class Solution {
#     def compareVersion(A: String, B: String): Int  = {
#       val aa = A.split('.')
#       val bb = B.split('.')
#       val zip = aa.zipAll(bb, "", "")
#       for (t2 <- zip) {
#         val s1 = t2._1.dropWhile(ch => ch == '0')
#         val s2 = t2._2.dropWhile(ch => ch == '0')
#         if (!(s1.isEmpty && s2.isEmpty)) {
#           if (s1.length > s2.length) return 1
#           else if (s1.length < s2.length) return -1
#           else {
#             val v1 = s1.toLong
#             val v2 = s2.toLong
#             if (v1 > v2) return 1
#             else if (v1 < v2) return -1
#           }
#         }
#       }
#       0
#     }
# }

# C++
# int Solution::compareVersion(string A, string B) {
#     // Do not write main() function.
#     // Do not read input, instead use the arguments to the function.
#     // Do not print the output, instead return values as specified
#     // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
#     int j, i;
#     for( i=0, j=0 ; i<A.size() || j<B.size() ; i++, j++){
#         unsigned long long num1 = 0, num2 = 0;
#         while(i < A.size() && A[i] != '.'){
#             num1 *= 10;
#             num1 += A[i] - '0';
#             i++;
#         }
#         while(j < B.size() && B[j] != '.'){
#             num2 *= 10;
#             num2 += B[j] - '0';
#             j++;
#         }
#         if(num1 > num2) return 1;
#         if(num1 < num2) return -1;
#     }
#     return 0;
# }

# GO
# /**
#  * @input A : String
#  * @input B : String
#  * 
#  * @Output Integer
#  */
 
#  import (
#  "strings"
#  "strconv"
# // "fmt"
#  )
 
# func compareStrings(one, two string) int {
#     one = strings.Trim(one, " ")
#     two = strings.Trim(two, " ")
# 	
#     one = strings.TrimLeft(one, "0")
#     two = strings.TrimLeft(two, "0")
# 	
#     if len(one) > len(two) {
#         return 1 
#     } else if len(one) < len(two) {
#         return -1
#     } else {
# 	    strLen := len(one)
#      	for  i := 0; i < strLen; i++ {
#     		if string(one[i]) > string(two[i]) {
#     			return 1
#     		} else if string(one[i]) < string(two[i]) {
#     			return -1
#     		} else {
#     			continue
#     		}
# 	    }
#     }	
#     return 0
# }


# func compareVersion(A string , B string )  (int) {
#     aVersion := strings.Split(A, ".")
#     bVersion := strings.Split(B, ".")
    
#     i := 0
#     j := 0
    
#     for ;i < len(aVersion) && j < len(bVersion); {
#         aVersion[i] = strings.Trim(aVersion[i], "\r")
#         bVersion[j] = strings.Trim(bVersion[j], "\r")
#         //strconv.ParseInt("-42", 10, 64)
#         //first, _ := strconv.ParseInt(aVersion[i], 10, 64)
#         //second, _ := strconv.ParseInt(bVersion[j], 10, 64)
#         //fmt.Println(first, second)
#         res := compareStrings(aVersion[i], bVersion[j])
#         if res == 1 {
#             return 1 
#         } else if res == -1 {
#             return -1
#         }
        
#         i++
#         j++
#     }

    
#     for ; i < len(aVersion);i++ {
#         aVersion[i] = strings.Trim(aVersion[i], "\r")
#         first, _ := strconv.ParseInt(aVersion[i], 10, 64)
#         //fmt.Println("i", aVersion[i], first)
#         if first == 0 {
#             continue
#         } else {
#             return 1
#         }
#     }
    
#     for ; j < len(bVersion);j++ {
#         //fmt.Println("j", aVersion[j])
#         bVersion[j] = strings.Trim(bVersion[j], "\r")
#         second, _ := strconv.ParseInt(bVersion[j], 10, 64)
#         if second == 0 {
#             continue
#         } else {
#             return -1
#         }
#     }
    
#     if i == len(aVersion) - 1 && j == len(bVersion) - 1 {
#         return 0
#     }
    
#     return 0
    
# }