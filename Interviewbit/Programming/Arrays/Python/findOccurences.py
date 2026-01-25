# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 13:17:14 2026

@author: USER
"""

'''
Problem Description
You are given an integer array A.
You have to find the number of occurences of each number.
Return an array containing only the occurences with the smallest value's occurence first.
For example, A = [4, 3, 3], you have to return an array [2, 1], where 2 is the number of occurences for element 3, 
and 1 is the number of occurences for element 4. But, 2 comes first because 3 is smaller than 4.

Problem Constraints
1 <= |A| <= 105
1 <= Ai <= 109
Input Format
The first argument is the integer array A.
Output Format
Return an integer array denoting the occurences of each number.
Example Input
Input 1:
A = [1, 2, 3]
Input 2:
A = [4, 3, 3]
Example Output
Output 1:
[1, 1, 1]
Output 2:
[2, 1]
Example Explanation
Explanation 1:
All the elements occur once, so the resultant array should be [1, 1, 1].
Explanation 2:
Explained in the description above.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):

'''

def findOccurences(A):
    dict_A = {}    
    for i in A:
        if i in dict_A:
            dict_A[i] += 1
        else:
            dict_A[i] = 1
    keys_list = list(dict_A.keys())
    keys_list.sort()
    result = []
    for j in keys_list:
        result.append(dict_A[j])
    return result

findOccurences(A)

'''
from collections import Counter
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, a):
        return [v for _, v in sorted(Counter(a).items())]
c++
vector<int> Solution::findOccurences(vector<int> &A) {
    map<int, int> mp;
    for(auto &x : A){
        mp[x]++;
    }
    vector<int> ans;
    for(auto &x : mp){
        ans.push_back(x.second);
    }
    return ans;
}    
Scala
import scala.collection.mutable
class Solution {
    def findOccurences(A: Array[Int]): Array[Int]  = {
        val m = mutable.Map[Int,Int]()
        A.foreach { v =>
            m.put(v, m.getOrElse(v, 0)+1)
        }
        val sortedKeys = m.keySet.toArray.sorted
        val ret = Array.fill(sortedKeys.length)(0)
        var idx = 0
        sortedKeys.foreach { k =>
            ret(idx) = m(k)
            idx = idx+1
        }
        ret

    }
}
GO:
    /**
 * @input A : Integer array
 * 
 * @Output Integer array.
 */
 
import "sort"

func findOccurences(A []int )  ([]int) {
    frequencyMap := make(map[int]int)
    for i:= 0 ; i< len(A) ;i ++ {
        frequencyMap[A[i]] = frequencyMap[A[i]] + 1 
    }
    keysInOrder := []int{}
    for k,_ := range(frequencyMap) {
        keysInOrder = append(keysInOrder, k)
    } 
    sort.Ints(keysInOrder)
    ans := []int{}
    for i := 0 ; i< len(keysInOrder) ; i ++ {
        ans = append(ans, frequencyMap[keysInOrder[i]])
    }
    return ans
}

    
'''
