# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 22:57:50 2026

@author: USER
"""

"""
Problem Description

Given a number A. Find the fatorial of the number.
Problem Constraints
1 <= A <= 100
Input Format
First and only argument is the integer A.

Output Format
Return a string, the factorial of A.

Example Input
Input 1:
A = 2
Input 2:
A = 3

Example Output
Output 1:
 2
Output 2:
 6

Example Explanation
Explanation 1:
2! = 2 .
Explanation 2:
3! = 6 .
class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):

"""

def solve(A):
    result = 1
    # n = A
    while A > 0:
        result *= A
        A -= 1
    return str(result)
# solve(3)        

# Scala
'''
class Solution {
    def solve(A: Int): String  = {
        @scala.annotation.tailrec
        def helper(n: Int, acc: BigInt =1): BigInt = {
          n match {
            case 1 => acc
            case _ => helper(n -1, acc * n)
          }
        }
        helper(A).toString    
        
        
    }
}

'''

# GO

'''
/**
 * @input A : Integer
 * 
 * @Output string.
 */
func solve(n int )  (string) {
    if n > 100 {
        fmt.Println("Too large a number... ")
        return ""
    }
    if n == 1 {
        s:="1"
        return s
    }
    arr := []int{1}
    arr[0] = 1
    for i:=2;i<=n; i++{
        rem :=0
        cry :=0
        for j:=0;j<len(arr); j++{
                curr := (arr[j] * i) + cry
                rem = curr  % 10
                cry =  curr  / 10
                arr[j] = rem
        }
        for ; cry > 0 ; {
            arr = append(arr,cry%10)
            cry = cry / 10
        }
    }
    for left, right := 0, len(arr)-1; left < right; left, right = left+1, right-1 {
        arr[left], arr[right] = arr[right], arr[left]
    }
    b := make([]string, len(arr))
    for i, v := range arr {
        b[i] = strconv.Itoa(v)
    }

    return strings.Join(b, "")
}


'''
# C++
'''
int multiply(int x, int res[], int res_size); 
#define MAX 500
// This function finds factorial of large numbers 
// and prints them 
string factorial(int n) 
{ 
    int res[MAX]; 
  
    // Initialize result 
    res[0] = 1; 
    int res_size = 1; 
  
    // Apply simple factorial formula n! = 1 * 2 * 3 * 4...*n 
    for (int x=2; x<=n; x++) 
        res_size = multiply(x, res, res_size); 
    string s="";
    for(int i=res_size-1;i>=0;i--)
        s+=res[i]+'0';
    return s;
} 
  
int multiply(int x, int res[], int res_size) 
{ 
    int carry = 0;  // Initialize carry 
  
    // One by one multiply n with individual digits of res[] 
    for (int i=0; i<res_size; i++) 
    { 
        int prod = res[i] * x + carry; 
  
        // Store last digit of 'prod' in res[]   
        res[i] = prod % 10;   
  
        // Put rest in carry 
        carry  = prod/10;     
    } 
  
    // Put carry in res and increase result size 
    while (carry) 
    { 
        res[res_size] = carry%10; 
        carry = carry/10; 
        res_size++; 
    } 
    return res_size; 
}
string Solution::solve(int A) {
    return factorial(A);
}
'''

#