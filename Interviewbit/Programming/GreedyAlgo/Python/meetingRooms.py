# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 14:54:03 2026

@author: mingt
"""

'''
Problem Description
Given an 2D integer array A of size N x 2 denoting time intervals of different meetings.
Where:
A[i][0] = start time of the ith meeting.
A[i][1] = end time of the ith meeting.
Find the minimum number of conference rooms required so that all meetings can be done.
Note :- If a meeting ends at time t, another meeting starting at time t can use the same conference room
Problem Constraints
1 <= N <= 105
0 <= A[i][0] < A[i][1] <= 2 * 109

Input Format
The only argument given is the matrix A.
Output Format
Return the minimum number of conference rooms required so that all meetings can be done.
Example Input
Input 1:
 A = [      [0, 30]
            [5, 10]
            [15, 20]
     ]
Input 2:
 A =  [     [1, 18]
            [18, 23]
            [15, 29]
            [4, 15]
            [2, 11]
            [5, 13]
      ]
Example Output
Output 1:

 2
Output 2:

 4


Example Explanation
Explanation 1:

 Meeting one can be done in conference room 1 form 0 - 30.
 Meeting two can be done in conference room 2 form 5 - 10.
 Meeting three can be done in conference room 2 form 15 - 20 as it is free in this interval.
Explanation 2:

 Meeting one can be done in conference room 1 from 1 - 18.
 Meeting five can be done in conference room 2 from 2 - 11.
 Meeting four can be done in conference room 3 from 4 - 15.
 Meeting six can be done in conference room 4 from 5 - 13.
 Meeting three can be done in conference room 2 from 15 - 29 as it is free in this interval.
 Meeting two can be done in conference room 4 from 18 - 23 as it is free in this interval.
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
'''

  A = [      [0, 30],
            [5, 10],
            [15, 20]
      ]
  solve(A)
# A
# # [(i, j[1]) for i, j in enumerate(A)]
# A.sort()

def solve(A):
    n_A = len(A)
    if n_A == 0:
        return 0
    
    start = [i[0] for i in A]
    end = [i[1] for i in A]
    start.sort()
    end.sort()
        
    pointer_front = 1 
    pointer_end = 0
    room_needed = 1
    room_maxed = 1
    
    while(pointer_front < n_A and pointer_end < n_A):
        if(start[pointer_front] < end[pointer_end]):
            room_needed += 1
            pointer_front += 1
        else:
            room_needed -= 1
            pointer_end += 1
        room_maxed = max(room_maxed, room_needed)
    return room_maxed
    # A.sort()
    # n_A = len(A)
    # list_end = [i[1] for i in A]
    # list_begin = [i[0] for i in A]
    # min_start = min(list_begin)    
    # # min_end = min(list_begin) 
    # max_end = max(list_end)
    # bool_A = [True] * n_A
    # # reseted = True
    # count = 0
    # cur_start = 0
    # cur_end = 0
    # for i in range(n_A):        
    #     if bool_A[i] != True:
    #         continue
    #     if i == n_A - 1:
    #         count += 1
    #         return count         
    #     for j in range(i+1, n_A):
    #         if 
''' solve2 use priority queue and solver1 use 2 pointers
int solve2(vector<vector<int> > &A){
    int n=A.size();
    sort(A.begin(),A.end());
        
        priority_queue<int, vector<int>, greater<int>> heap;
        int rooms = 0;
        heap.push(A[0][1]);
        rooms++;
        for (int i = 1; i < n; i++) {
            if (A[i][0] < heap.top()) {
                rooms++;
            } else {
                heap.pop();
            }
            heap.push(A[i][1]);
        }
        return rooms;
}

int solve1(vector<vector<int> > &A){
    int n=A.size();
    assert(1 <= n && n<= 100000);
     int start[n];
     int end[n];
     for (int i=0; i<n; i++) {
       start[i]=A[i][0];
       end[i]=A[i][1];
     }
     sort(start,start+n);
     sort(end,end+n);
     int i=0, j=0, res=0;
     while (i<n) {
       if (start[i]<end[j])
        i++;
       else if (start[i]>end[j])
        j++;
       else {
         i++;
         j++;
       }
       res=max(res,i-j);
     }
     return res;
}

int Solution::solve(vector<vector<int> > &A) {
    return solve1(A);
}

 #Scala:
class Solution {
    def solve(arr: Array[Array[Int]]): Int  = {
        val ar=arr.sortWith(_(0)<_(0))
        val dep=arr.sortWith(_(1)<_(1))
    
        var curPt = 1
        var maxPt = 1
        var i = 1
        var j = 0
        while (i < ar.length && j < dep.length) {
          //if(ar(i)<dep(j)){
          if(ar(i)(0)<dep(j)(1)){
            curPt+=1
            i+=1
            maxPt=math.max(curPt,maxPt)
          }else{
            curPt-=1
            j+=1
          }
        }
        return maxPt
    }
}

'''