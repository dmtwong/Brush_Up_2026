# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:05:13 2026

@author: USER
"""
"""
Problem Description
Given an one-dimensional unsorted array A containing N integers.
You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.
Return 1 if any such pair exists else return 0.
Problem Constraints
1 <= N <= 105
-103 <= A[i] <= 103
-105 <= B <= 105
Input Format
First argument is an integer array A of size N.
Second argument is an integer B.
"""
def solve(A, B):
    def merge(lf, rt, comp):
        result = []
        i, j = 0, 0
        n_lf = len(lf)
        n_rt = len(rt)
        while i < n_lf and j < n_rt:
            if comp(lf[i], rt[j]):
                result.append(lf[i])
                i += 1
            else:
                result.append(rt[j])
                j += 1
        while (i < n_lf):
            result.append(lf[i])
            i += 1
        while (j < n_rt):
            result.append(rt[j])
            j += 1            
        return result
    def mergeSort(A, comp = lambda x, y: x < y):
        n_A = len(A)
        if n_A < 2:
            return A[:]
        else:
            mid = n_A //2 
            lf = mergeSort(A[:mid], comp)
            rt = mergeSort(A[mid:], comp)
            return merge(lf, rt, comp)
    n_A = len(A)
    pos_B = abs(B)
    A = mergeSort(A)
    A_last = A[n_A - 1]
    
    for i in range(n_A - 1):
        A_i = A[i]
        lw_bound = A[i+1] - A_i
        up_bound = A_last - A_i
        # print(i, lw_bound, up_bound)
        if pos_B < lw_bound or pos_B > up_bound:
            # print('skip')
            continue
        for j in range(n_A - 1, i, -1):
            temp = A[j] - A_i
            if temp == pos_B:
                return 1
            if temp < pos_B:
                A_i = j
    return 0

# Editorial
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        temp=dict()
        for a in A:
            try:
                temp[a]=temp[a]+1
            except KeyError:
                temp[a]=1
        for a in A:
            if((B+a)==a and temp[a]>1):
                return 1
            elif(B+a==a):
                continue
            elif(temp.get(B+a,0)!=0):
                return 1
        return 0
'''

# Scala:
'''
class Solution {
    def solve(A: Array[Int], B: Int): Int  = {
    
        import scala.collection.mutable
        import scala.collection.mutable.HashMap
        val arr = A.sorted
        val diff = B
        val map = new mutable.HashMap[Int, Boolean]()
        var status = false
    
        for(num <- arr) {
    
          if(map.contains(num)) {
            status = true
          } else {
            map.put(diff + num, true)
            map.put(num - diff, true)
          }
        }
        if(status) 1 else 0
    }
}
'''
# C++

'''
bool findPair(vector<int>&arr, int size, int n)  
{  
    // Initialize positions of two elements  
    int i = 0;  
    int j = 1;  
   sort(arr.begin(),arr.end());
    // Search for a pair  
    while (i < size && j < size)  
    {  
        if (i != j && arr[j] - arr[i] == n)  
        {
            return true;  
        }  
        else if (arr[j]-arr[i] < n)  
            j++;  
        else
            i++;  
    }  
    return false;  
}  
int Solution::solve(vector<int> &A, int B) {
    return findPair(A,A.size(),B);
}
'''

# GO
'''
/**
 * @input A : Integer array
 * @input B : Integer
 * 
 * @Output Integer
 */
func solve(A []int , B int )  (int) {
    m := make(map[int][]int)
    for i,a:=range A{
        m[a] = append(m[a],i)
    }
    for i:=0;i<len(A);i++{
        k := B + A[i]
        if _,ok:=m[k];ok{
            val := m[k]
            for j:=0;j<len(val);j++{
                if val[j] != i{
                    return 1
                }
            }
        }
    }
    return 0
}
'''