//============================================================================
// Name        : balancedParantheses.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

/*
 * Problem Description
Given a string A consisting only of '(' and ')'.
You need to find whether parantheses in A is balanced or not ,if it is balanced then return 1 else return 0.
Problem Constraints
1 <= |A| <= 105

Input Format
First argument is an string A.

Output Format
Return 1 if parantheses in string are balanced else return 0.

Example Input
Input 1:
 A = "(()())"
Input 2:
 A = "(()"
Example Output
Output 1:
 1
Output 2:
 0
Example Explanation
Explanation 1:
 Given string is balanced so we return 1
Explanation 2:
 Given string is not balanced so we return 0
 */
#include <iostream>
#include <stack>
#include <map>
#include <string>

using namespace std;


//int Solution::solve(string A) {
int solve(string A) {
    stack<char> s;
    // map<char, char> matching_pair = { {')', '('} };
    for (char i : A) {
        if (i == '(') {
            s.push(i);
        }
        else if (i == ')') {
            if (s.empty()) {
                return 0;
            }
            // if (s.top() == '(') { // matching_pair[character]) {
            s.pop(); // Pop the matching opening bracket
            //} else {
            //    return 0; // Mismatched brackets
            }
        }
    if (s.empty()){
	    return 1;
    } else {
        return 0;
    }
}
/*
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
*/

/*
 *
 * int Solution::solve(string A)
{
    stack<int> s;
    for(int i=0;i<A.size();i++)
    {
        if(A[i]=='(')
        {
            s.push(i);
        }
        else
        {
            if(s.empty())
            {
                return 0;
            }
            s.pop();
        }
    }
    return s.empty();

}

/*def solveQ(A):
    stk=[]
    for a in A:
        if(a=='('):
            stk.append(a)
            continue
        if(len(stk)==0):
            return False
        if(a==')'):
            x=stk[-1]
            stk.pop(-1)
            if(x!='('):
                return False
    if(len(stk)==0):
        return True
    return False

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if(solveQ(A)==False):
            return 0
        return 1
        */

// Scala:
/*
 * class Solution {
    def solve(A: String): Int  = {
        var openBrackets = 0

        for (c <- A) {
            c match{
                case '(' => openBrackets += 1
                case ')' => if (openBrackets == 0) return 0 else openBrackets -= 1
            }
        }
        return if (openBrackets > 0)  0 else 1
    }
}
 *
 */

// GO
/**
 * @input A : String
 *
 * @Output Integer
 */
/*
func solve(A string )  (int) {
    stack := []byte{}

    for _, val := range A {
        if val == '(' {
            stack = append(stack, '(')
        } else {
            if len(stack) == 0 {
                return 0
            }

            stack = stack[0:len(stack)-1]
        }
    }

    if len(stack) > 0 {
        return 0
    }

    return 1
}
*/
