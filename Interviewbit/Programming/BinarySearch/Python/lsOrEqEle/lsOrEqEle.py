# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 22:03:26 2026

@author: USER
"""
'''
Problem Description
Given an sorted array A of size N. 
Find number of elements which are less than or equal to B.
NOTE: Expected Time Complexity O(log N)

Problem Constraints
1 <= N <= 106
1 <= A[i], B <= 109

Input Format
First agument is an integer array A of size N.
Second argument is an integer B.

Output Format
Return an integer denoting the number of elements which are less than or equal to B.
Example Input
Input 1:
 A = [1, 3, 4, 4, 6]
 B = 4
Input 2:
 A = [1, 2, 5, 5]
 B = 3
Example Output
Output 1:
 4
Output 2:
 2
 
 class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
'''
def solve(A, B):
    def bS(A, B, low, high):
        if low == high:
            if A[low] == B:
                # print(low)
                return low
        mid = (low + high) // 2
        # print(low, high, mid)
        if A[mid] == B:
            # print(mid)
            return mid
        elif A[mid] > B:
            if low != mid:
                return bS(A, B, low, mid)
            else: 
                return 0
        else:
            return bS(A, B, mid + 1, high)
    n_A = len(A)
    if n_A == 0 or A[0] > B:
        return 0
    elif A[n_A - 1] <= B:
            return n_A
    else:
        ix = bS(A, B, 0, n_A - 1)
        # print(ix)
        if A[ix] != B:
            count = 0
            while A[ix] < B:
                count += 1
                ix += 1
            return count
        else:
            count = ix + 1
            # print(count)
            while ix < (n_A - 1):
                ix += 1
                if A[ix] == B:
                    count += 1
                else:
                    # print(ix, count)
                    return count             

# Editorial
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        left = 0
        right = n - 1
      
        count = 0
      
        while (left <= right):  
            mid = int((right + left) / 2) 
      
            # Check if middle element is less than or equal to B
            if (A[mid] <= B):  
      
                # At least (mid + 1) elements are there whose values are less than or equal to key 
                count = mid + 1
                left = mid + 1
              
            # If B is smaller, ignore right half 
            else: 
                right = mid - 1
          
        return count 
'''

# Scala
'''
class Solution {
    def solve(A: Array[Int], B: Int): Int  = {
        import scala.collection.Searching._
        val ip=A.search(B)
        if(ip.isInstanceOf[InsertionPoint]){
            return ip.insertionPoint
        }else{
            var j=ip.insertionPoint+1
            while(j<A.length && A(j)==B) j+=1
            return j
        }
    }
}
'''

# C++
'''
int Solution::solve(vector<int> &A, int B) {
    int n = A.size();
    int left = 0;
    int right = n - 1;
    int count = 0;

    while (left <= right) {
        int mid = (right + left) / 2;

        // Check if middle element is less than or equal to B
        if (A[mid] <= B) {

            // At least (mid + 1) elements are there whose values are less than or equal to B
            count = mid + 1;
            left = mid + 1;
        }

        // If B is smaller, ignore right half
        else
            right = mid - 1;
    }
    return count;
    
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
 
// import "fmt"

func solve(A []int , B int )  (int) {
    l, r := 0, len(A)
    
    for l <= r {
        mid := (l+r)/2
        // fmt.Println(mid)
        
        if mid == 0 || (A[mid-1] <= B && (mid == len(A) || A[mid] > B)) {
            return mid
        } else if A[mid] <= B {
            l = mid+1
        } else {
            r = mid
        }
    }
    
    return -1
}

'''
