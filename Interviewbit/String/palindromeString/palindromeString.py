# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 19:13:25 2026

@author: USER
"""

'''
Problem Description
Given a string, determine if it is a palindrome. While checking for a palindrome, you have to ignore spaces, case, and all special characters; i.e. consider only alphanumeric characters.
Check the sample test case for reference.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Problem Constraints
1 <= |A| <= 106
Input Format
The first argument is a string A.
Output Format
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Example Input
Input 1:
A = "A man, a plan, a canal: Panama"
Input 2:
B = "race a car"
Example Output
Output 1:
1
Output 2:
0
Example Explanation
Explanation 1:
The input string after ignoring spaces, and all special characters is "AmanaplanacanalPanama" 
which is a palindrome after ignoring the case.
Explanation 2:
The input string after ignoring spaces, and all special characters is "raceacar" which is not a palindrome
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
'''
def isPalindrome(A):
    alphaNum = 'abcdefghijklmnopqrstuvwxyz' + ''.join([str(i) for i in range(10)])
    def isPal(B):
        n_B = len(B)
        if n_B <= 1:
            return 1
        for i in range(n_B // 2):
            if B[i] != B[-(i+1)]:
                return 0
            else:
                return 1 and isPal(B[1:(n_B-1)])
    def prettyString(B):
        low_B = B.lower()
        new_B = ''
        for i in low_B:
            # print(i)
            if i in alphaNum:
                # print(new_B)
                new_B = i + new_B
                # print(new_B)
            # print('!!')
        # print(new_B)
        return new_B
    return isPal(prettyString(A))

# Python (Editorial)
'''
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A = A.lower()
        n = len(A)
        low = 0
        high = n - 1
        ret = 1
        while low <= high:
            if A[low] == A[high]:
                low += 1
                high -= 1
                continue
            if str(A[low]).isalnum() and str(A[high]).isalnum():
                ret = 0
                break
            elif str(A[high]).isalnum():
                low += 1
            else:
                high -= 1
        return ret
'''

# Scala
'''
class Solution {
    def isPalindrome(A: String): Int  = {
        if (A.isEmpty()) {
        	return 1;
        }
        var head: Int = 0;
        var tail: Int = A.length()-1;
        var cHead: Char = 'a';
        var cTail: Char = 'a';
        while(head <= tail) {
        	cHead = A.charAt(head);
        	cTail = A.charAt(tail);
        	if (!Character.isLetterOrDigit(cHead)) {
        		head = head + 1;
        	} else if(!Character.isLetterOrDigit(cTail)) {
        		tail = tail - 1;
        	} else {
        		if (Character.toLowerCase(cHead) != Character.toLowerCase(cTail)) {
        			return 0;
        		}
        		head = head + 1;
        		tail = tail - 1;
        	}
        }
        
        return 1;
    }
}

'''

# C++

'''
int Solution::isPalindrome(string A) {
    int i = 0, j = (int)A.size() - 1;
    while(i < j)
    {
        while(i < j && !isalnum(A[i])) i++;
        while(i < j && !isalnum(A[j])) j--;
        if (toupper(A[i]) != toupper(A[j])) return false; 
        i++;
        j--;
    }
    return true;
}
'''

# GO
'''
import(
    "strings"
)
func isPalindrome(A string )  (int) {
	
	runes := []rune(A)
	str := []rune{}
	for i := 0; i < len(runes); i++ {
		if (runes[i] >= 'a' && runes[i] <= 'z') || (runes[i] >= 'A' && runes[i] <= 'Z') || (runes[i] >= '0' && runes[i] <= '9') {
			str = append(str, runes[i])
		}
	}
	str = []rune(strings.ToLower(string(str)))
	for i := 0; i < len(str) / 2; i++ {
		if str[i] != str[len(str) - 1 - i] {
			return 0
		}
	}
	
	return 1
}
'''