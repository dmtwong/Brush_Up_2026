//============================================================================
// Name        : revStr.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

/*
 * Given a string S, reverse the string using stack.
Example :
Input : "abc"
Return "cba"
PROBLEM APPROACH :
Complete solution in hints.
 */
#include <iostream>
#include <string>
#include <stack>
#include <algorithm>
// #include <cstring>
using namespace std;

//int main() {
	//cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//return 0;
	// string Solution::reverseString(string A) {
	string reverseString(string A) {
	    std::stack<char> stack_char;
	    std::string result = "";

	    for (char c : A) {
	    	stack_char.push(c);
	    }

	    while (!stack_char.empty()) {
	    	result += stack_char.top();
	    	stack_char.pop();
	    }

	    return result;
	}

//}

/*
string Solution::reverseString(string A) {
   string str{};
   stack<char>s;
   for(int i{};i<A.length();i++){
       s.push(A[i]);
   }
   for(int i=0;i<A.length();i++){
       str = str + s.top();
       s.pop();
   }
   return str;
}


 */

/* Scala:
class Solution {
    def reverseString(A: String): String  = {
      import scala.collection.mutable
      val queue = mutable.Stack[Char]()
      for(ch <- A) queue.push(ch)
      var ret = ""
      while (queue.nonEmpty) ret += queue.pop()
      ret
    }
}
 */

/* GO:
**
 * @input A : String
 *
 * @Output string.
 /
func reverseString(A string )  (string) {
    l := len(A)
    if l <= 1 {
        return A
    }


    result := ""
    for i := 1; i <= l; i++ {
        result += string(A[l - i])
    }
    return result
}



	 */

/* Python
 *class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        revA = []
        for a in A:
            revA.insert(0,a)
        return ''.join(revA)
 */



