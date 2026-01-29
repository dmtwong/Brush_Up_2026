# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 13:01:40 2026

@author: mingt
"""
'''
Problem Description
Say you have an array, A, for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Problem Constraints
0 <= len(A) <= 1e5
1 <= A[i] <= 1e7
Input Format
The first and only argument is an array of integers, A.
Output Format
Return an integer, representing the maximum possible profit.
Example Input
Input 1:
    A = [1, 2, 3]
Input 2:
    A = [5, 2, 10]
Example Output
Output 1:
    2
Output 2:
    8
Example Explanation
Explanation 1:
    => Buy a stock on day 0.
    => Sell the stock on day 1. (Profit +1)
    => Buy a stock on day 1.
    => Sell the stock on day 2. (Profit +1)
Overall Profit = 2
Explanation 2:
    => Buy a stock on day 1.
    => Sell the stock on on day 2. (Profit +8)
Overall profit = 8
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
'''
def maxProfit(A):
    profit = 0
    # hold = 0 
    n_A = len(A)
    for i in range(1, n_A):
        price_i = A[i]
        price_lag = A[i-1]
        earning = price_i - price_lag
        if (earning < 0):
            continue
        else:
            profit += earning
    return profit

'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        n = len(A)
        
        if n <= 1:
            return 0
        
        total_profit = 0
        
        i = 0
        j = 1
        
        while j < n:
            if A[j] > A[i]:                
                profit = A[j] - A[i]
                total_profit += profit
    
            i += 1
            j += 1
            
        return total_profit
int Solution::maxProfit(const vector<int> &A) {
    // Prices must be given for at least two days
    if (A.size() <= 1) {
        return 0;
    }
 
    int count = 0; // count of solution pairs
    int n = A.size();
    // solution vector
    int buy[n/2 + 1], sell[n/2 + 1];
 
    // Traverse through given price array
    int i = 0;
    while (i < n-1)
    {
        // Find Local Minima. Note that the limit is (n-2) as we are
        // comparing present element to the next element. 
        while ((i < n-1) && (A[i+1] <= A[i]))
            i++;
 
        // If we reached the end, break as no further solution possible
        if (i == n-1)
            break;
 
        // Store the index of minima
        buy[count] = i++;
 
        // Find Local Maxima.  Note that the limit is (n-1) as we are
        // comparing to previous element
        while ((i < n) && (A[i] >= A[i-1]))
            i++;
 
        // Store the index of maxima
        sell[count] = i-1;
 
        // Increment count of buy/sell pairs
        count++;
    }
 
    // print solution
    if (count == 0)
        return 0;
    else
    {
        int ret = 0;
        for (int i = 0; i < count; i++) {
            ret += A[sell[i]] - A[buy[i]];
            //printf("Buy on day: %d\t Sell on day: %d\n", sol[i].buy, sol[i].sell);
        }
        return ret;
    }
}

# Scala:
    class Solution {
    def maxProfit(A: Array[Int]): Int  = {
        var maxProfit = 0
        for(i <- 0 until A.length -1) {
          if(A(i+1)>=A(i)) {
            maxProfit += A(i+1) - A(i) 
          }
        }
        maxProfit
    }
}

# GO:
/**
 * @input A : Integer array
 * 
 * @Output Integer
 */

func maxProfit(A []int )  (int) {
    var profit int
    buyIndex := 0
    for buyIndex < len(A) {
        sellIndex := buyIndex + 1
        for sellIndex < len(A) && A[sellIndex] > A[sellIndex - 1] {
            sellIndex++
        }
        currProfit := A[sellIndex - 1] - A[buyIndex]
        if currProfit > 0 {
            profit = profit + currProfit
        }
        buyIndex = sellIndex
    }
    return profit
}
'''
            
    
    



