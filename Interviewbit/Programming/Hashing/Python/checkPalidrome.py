# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 13:08:24 2026

@author: USER
"""
'''
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
'''
def solve(A):
    dict_let = {}
    for i in A:
        # print(i)
        if i in dict_let:
            # print(dict_let)
            dict_let[i] += 1
        else:
            dict_let[i] = 1
    odd_occ = [i % 2 for i in dict_let.values()]
    buffer = True
    for i in odd_occ:
        if i == 1:
            if buffer == False:
                return 0
            else:
                buffer = False
    return 1
            
A = "inttnikjmjbemrberk"           
solve(A)

'''
# function to check whether characters 
# of a string can form a palindrome  
def canFormPalindrome(st) : 
  
    # Create a count array and initialize   
    # all values as 0 
    count = [0] * (26) 
  
    # For each character in input strings, 
    # increment count in the corresponding 
    # count array 
    for i in range( 0, len(st)) : 
        count[ord(st[i])-ord('a')] = count[ord(st[i])-ord('a')] + 1
  
    # Count odd occurring characters 
    odd = 0
      
    for i in range(0, 26) : 
        if (count[i] & 1) : 
            odd = odd + 1
  
        if (odd > 1) : 
            return False
              
    # Return true if odd count is 0 or 1,  
    return True
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if(canFormPalindrome(A)):
            return 1
        return 0
    
int Solution::solve(string A) {
  int hashMap[26] = {0};
  for (char a: A)
    hashMap[a - 'a']++;
  int odd = 0;
  for (int a: hashMap)
    if (a % 2)
      odd++;
  if (odd > 1)
    return 0;
  return 1;
}

import scala.collection.mutable.HashMap
class Solution {
    def solve(A: String): Int = {
    var flag: Boolean = false
    val map = HashMap[Char, Int]()
    for (a <- A) {
      map.update(a, map.getOrElse(a, 0) + 1)
    }
    for ((x, v) <- map) {
      if (v % 2 == 1)
        if(!flag && A.length % 2 == 1) flag = true
        else return 0
      }
    1
  }
}

/**
 * @input A : String
 * 
 * @Output Integer
 */
func solve(A string )  (int) {
    m := make(map[rune]int)
    isOdd := len(A) % 2
    oddChar := 0
    for _, r := range A {
        m[r]++
    }
    for _, v := range m {
        if v % 2 == 1 {
            oddChar++
        }
        if oddChar > isOdd {
            return 0
        }
    }
    return 1
}

    
'''
