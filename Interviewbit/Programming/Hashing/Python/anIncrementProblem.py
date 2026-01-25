# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 15:37:29 2026

@author: USER
"""
'''
Problem Description
Given a stream of numbers A. On arrival of each number, you need to increase its first occurrence by 1 and include this in the stream.
Return the final stream of numbers.
Note: You will traverse the stream from left to right and update the first occurrence of the number by 1, if found.
Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10000

Input Format
First and only argument is the array A.

Output Format
Return an array, the final stream of numbers.

Example Input
Input 1: 
A = [1, 1]
Input 2:
A = [1, 2]
 
Input 3:
A = [1, 1, 2, 2]
Example Output
Output 1:
[2, 1]
 
Output 2:
[1, 2]
 
Output 3:
[3, 1, 3, 2]
Example Explanation
Explanation 1:
On arrival of the second element, the other element is increased by 1.

Explanation 2:
No increases are to be done.
 
Explanation 3:
Stream after arrival of numbers (1-based indexing):
  First number  (1): [1]          , Simply push 1 to the stream
  Second number (1): [2, 1]       , Increment first occurence of 1, present at 1st Index and push 1 to the stream
  Third number  (2): [3, 1, 2]    , Increment first occurence of 2, present at 1st Index and push 2 to the stream
  Fourth number (2): [3, 1, 3, 2] , Increment first occurence of 2, present at 3rd Index and push 2 to the stream
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
'''
A = [1, 1, 2, 2]
# A = [3, 2, 1, 1]
# A.pop()
# solve(A)
def solve(A):
    # n_A = len(A)
    # dict_A = {}    
    result = []
    for i in A:
        if i in result:
            ix = result.index(i)
                result[ix] += 1
        result.append(i)        
    return result

    # for i in range(n_A):
    #     flag_update = False
    #     A_i = A[i] 
    #     if A_i not in dict_A:
    #         dict_A[A_i] = i
    #     else:
    #         flag_update = True
    #         while flag_update == True:
    #             ix = dict_A[A_i]
    #             print('here', ix, A_i)
    #             print(dict_A)
    #             # del dict_A[A_i]
    #             A[ix] += 1
    #             print(dict_A, A[ix], A, A[i])
    #             A_i = A[ix]
    #         #     dict_A[A_i].pop(0)
    #             if A_i not in dict_A:
    #                 print('there', ix, A_i)
    #                 print(dict_A)
    #                 print(dict_A, A[ix], A)
    #                 flag_update = False
    #                 dict_A[A_i] = i
    #             else:
    #                 ix = dict_A[A_i]
    #                 del dict_A[A_i]
    #                 print(ix, A_i)
    #                 print(dict_A)
    #                 print(dict_A, A[ix], A)
    #                 A[ix] += 1
    #                 A_i = A[ix]
    #         #         dict_A[A_i.append[i]]
    # return A
solve(A)

''' Editorial
class Solution:
    # @param A : list of integers
    # @return a list of integers
    
    def solve(self, A):
        import heapq

        occurence_index = {}
        final = []
        for i, a in enumerate(A):
            oi = occurence_index.setdefault(a, [])
            heapq.heappush(oi, i) 
            occurence_index[a] = oi
            final.append(a)
            
            if len(oi) > 1:
                idx_to_change = heapq.heappop(oi)
                final[idx_to_change] += 1
                heapq.heappush(occurence_index.setdefault(final[idx_to_change], []), idx_to_change)
        return final

vector<int> Solution::solve(vector<int> &A) {
    vector<int> res;
    for(int i=0;i<A.size();i++) {
        auto it=find(res.begin(),res.end(),A[i]);
        if(it!=res.end()) {
            (*it)++;
            res.push_back(A[i]);
        }
        else {
            res.push_back(A[i]);
        }
    }
    return res;
}

Scala:
    class Solution {
    def solve(A: Array[Int]): Array[Int]  = {

    def loop(i: Int, cache: Map[Int, Int]): Array[Int] = {
      if (i == A.length) A
      else {
        val nCache =
          if (cache.contains(A(i))) {
            val oldPos = cache(A(i))
            val newVal = A(oldPos) + 1

            // update the array and add the new element to the cache
            A(oldPos) = newVal

            // if the new value, ie the old one increment of one unit
            // is already present in the cache, update the index to the min
            // otherwise add it as a new item to the cache
            if (cache.contains(newVal))
              cache + (newVal -> Math.min(oldPos, cache(newVal)))
            else
              cache + (newVal -> oldPos)
          }
          else cache
        loop(i + 1, nCache + (A(i) -> i))
      }
    }

    loop(0, Map.empty[Int, Int])
  }


}

# GO
/**
 * @input A : Integer array
 * 
 * @Output Integer array.
 */
func solve(A []int )  ([]int) {
    m := make(map[int]int)
    
    for i, v := range A {
        if _, ok := m[v]; ok {
            A[m[v]]++
            m[A[m[v]]] = m[v]
            m[v] = i
        } else {
            m[v] = i
        }
    }
    return A
}

'''
