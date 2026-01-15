# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 17:49:41 2026
@author: USER
"""

"""
Print concentric rectangular pattern in a 2d matrix. 
Let us show you some examples to clarify what we mean.

Example 1:
Input: A = 4.
Output:
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

Example 2:
Input: A = 3.
Output:
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.
You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
Note:You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified. Still have a question? Checkout Sample Codes for more details.
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
"""
def prettyPrint(A):
    n = A*2 - 1
    # result = [[] for i in range(n)] 
    result = []
    for i in range(A):
        rw = [] 
        val_i = A
        
        for j in range(i):
            rw.append(val_i)
            val_i -= 1                
        
        for k in range(n - 2 * i):
            rw.append(A - i)
        
        val_i = A - i + 1
        for l in range(i):
            rw.append(val_i)
            val_i += 1            
        
        result.append(rw) 
    
    for i in range(A-2, -1, -1):
        result.append(result[i][:])
        
    return result

    # for i in range(n):
    #     row_i = [A] * n
    #     ix = i
    #     # adj_counter = adj
    #     off = 0
    #     for j in range(A):
    #         while ix > 0:
    #             off += 1
    #             row_i[j+1] -= off
    #             row_i[n-j] -= off
    #             ix -= 1            
    #         # off += 1
            
    #         if i != n - 1:
    #             print(i, -(i+1))
    #             print(result[i])
    #             print(row_i)
    #             # result[i], result[-(i+1)] = row_i, row_i
    #             result[i] = row_i
    #             result[-(i+1)] = row_i
    #         else:
    #             result[i] = row_i
