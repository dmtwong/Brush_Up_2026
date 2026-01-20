# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 17:06:26 2026

@author: USER
"""

# An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each string may be an integer or an operator.
# Problem Constraints
# 1 <= N <= 105
# Input Format
# The only argument given is string array A.
# Output Format
# Return the value of arithmetic expression formed using reverse Polish Notation.
# Example Input
# Input 1:
    # A =   ["2", "1", "+", "3", "*"]
    # evalRPN(A)
# Input 2:
    # A = ["4", "13", "5", "/", "+"]
# Example Output
# Output 1:
#     9
# Output 2:
#     6
# Example Explanation
# Explaination 1:
#     starting from backside:
#     * : () * ()
#     3 : () * (3)
#     + : (() + ()) * (3)
#     1 : (() + (1)) * (3)
#     2 : ((2) + (1)) * (3)
#     ((2) + (1)) * (3) = 9
# Explaination 2:
#     + : () + ()
#     / : () + (() / ())
#     5 : () + (() / (5))
#     13 : () + ((13) / (5))
#     4 : (4) + ((13) / (5))
#     (4) + ((13) / (5)) = 6
# class Solution:
# 	# @param A : list of strings
# 	# @return an integer
# 	def evalRPN(self, A):
    
def evalRPN(A):
    stack_A = []
    n_A = len(A) 
    if n_A == 0:
        return 0
    elif n_A == 1:
        return int(A[0])    
    for i in A:
        if i in ('+', '-', '*', '/'):
            b = stack_A.pop()
            a = stack_A.pop()
            if i == '+':
                result = a + b
            elif i == '-':
                result = a - b
            elif i == '*':
                result = a * b
            elif i == '/':
                result = a // b
            stack_A.append(result)
        else:
            stack_A.append(int(i))
    return stack_A.pop()

# Editorial
# from operator import *
# from itertools import starmap 
# class Solution:
#     # @param A : list of strings
#     # @return an integer
#     def evalRPN(self, A):
#         D = dict(zip("+-*/", [add, sub, mul, floordiv]))
#         S = []
#         for a in A:
#             if a in D:
#                 x, y = S.pop(), S.pop()
#                 S.append(D[a](y, x)) 
#             else:
#                 S.append(int(a))
#         return S[0]

# int Solution::evalRPN(vector<string> &tokens) {
#     stack<int> st;
#             for(int i = 0; i < tokens.size(); ++i) {
#                 if(tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/") {
#                     int v1=st.top();
#                     st.pop();
#                     int v2=st.top();
#                     st.pop();
#                     switch(tokens[i][0]) {
#                         case '+':
#                             st.push(v2 + v1);
#                             break;
#                         case '-':
#                             st.push(v2 - v1);
#                             break;
#                         case '*':
#                             st.push(v2 * v1);
#                             break;
#                         case '/':
#                             st.push(v2 / v1);
#                             break;
#                     }
#                 } else {
#                     st.push(atoi(tokens[i].c_str()));
#                 }
#             }
#             return st.top();
# }

# Scala
# class Solution {
#     def evalRPN(A: Array[String]): Int  = {
#       import scala.collection.mutable
#       val stack = mutable.Stack[Int]()
#       for (ai <- A) {
#         ai match {
#           case "+" => stack.push(stack.pop() + stack.pop())
#           case "*" => stack.push(stack.pop() * stack.pop())
#           case "-" => {
#             val a1 = stack.pop()
#             val a2 = stack.pop()
#             stack.push(a2 - a1)
#           }
#           case "/" => {
#             val a1 = stack.pop()
#             val a2 = stack.pop()
#             stack.push(a2 / a1)
#           }
#           case ch => stack.push(ch.toInt)
#         }
#       }
#       stack.top
#     }
# }

# GO
# import "strconv"

# type myStack []int

# func (s myStack) Push(v int) myStack {
# 	return append(s, v)
# }

# func (s myStack) Pop() (myStack, int) {
# 	l := len(s)
# 	return s[:l-1], s[l-1]
# }

# func (s myStack) isEmpty() bool {
# 	return len(s) == 0
# }

# func evalRPN(exp []string) (int) {
# 	stack := myStack{}
# 	var op1, op2 int
# 	for i := 0; i < len(exp); i++ {
# 		if exp[i] != "+" && exp[i] != "-" && exp[i] != "*" && exp[i] != "/" {
# 			val, _ := strconv.Atoi(exp[i])
# 			stack = stack.Push(val)
# 		} else if exp[i] == "+" {
# 			stack, op1 = stack.Pop()
# 			stack, op2 = stack.Pop()
# 			stack = stack.Push(op2 + op1)
# 		} else if exp[i] == "-" {
# 			stack, op1 = stack.Pop()
# 			stack, op2 = stack.Pop()
# 			stack = stack.Push(op2 - op1)
# 		} else if exp[i] == "*" {
# 			stack, op1 = stack.Pop()
# 			stack, op2 = stack.Pop()
# 			stack = stack.Push(op2 * op1)
# 		} else if exp[i] == "/" {
# 			stack, op1 = stack.Pop()
# 			stack, op2 = stack.Pop()
# 			stack = stack.Push(op2 / op1)
# 		}
# 	}
# 	
# 	var res int
# 	stack, res = stack.Pop()
# 	
# 	return res
# }