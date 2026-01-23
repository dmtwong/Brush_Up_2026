//============================================================================
// Name        : maxString.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
/*
 *Problem Description
Given a string A and integer B, what is maximal lexicographical string that can be made from A if you do atmost B swaps.
Problem Constraints
1 <= |A| <= 9
A contains only digits from 0 to 9.
1 <= B <= 5
Input Format
First argument is string A.
Second argument is integer B.
Output Format
Return a string, the naswer to the problem.
Example Input
Input 1:
A = "254"
B = 1
Input 2:
A = "254"
B = 2
Example Output
Output 1:
 524
Output 2:
 542
Example Explanation
Explanation 1:
 Swap 2 and 5.
Explanation 2:
Swap 2 and 5 then swap 4 and 2.
 *
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
 */
#include <iostream>
#include <utility>
#include <utility>
#include <string>

using namespace std;

void helper(string A, int B, string &larger){
	    if(B == 0 or A.length() == 1){
	        return;
	    }
	    for(int i = 0; i < A.length(); i++){
	        for(int j = i+1; j < A.length(); j++){
	            swap(A[i], A[j]);
	            if(A > larger){
	            	larger = A;
	            }
	            helper(A, B-1, larger);
	            swap(A[i], A[j]);
	        }
	    }
}

//string Solution::solve(string A, int B) {
string solve(string A, int B) {
    string maxi = A;
    helper(A, B, maxi);
    return maxi;
}

/*void swap(char &a,char &b)
{
    char c=a; a=b; b=c;
}

string ans;
int n;

void check(int i,string &str,int k)
{
    if(ans<str)
    ans=str;

    if(!k || i==n)
    return;

    check(i+1,str,k);

    for(int j=i+1;j<n;j++)
    {
        if(str[j]>str[i])
        {
            swap(str[j],str[i]);
            check(i+1,str,k-1);
            swap(str[j],str[i]);
        }
    }
}
string Solution::solve(string str, int k)
{
     ans=str;
    n=str.length();

     check(0,str,k);
     return ans;
}

    def solve(self, A, B):
        if len(A) == 1 or B == 0:
            return A
        combinations = []
        for (i, s) in enumerate(A):
            currString = s + A[1:i] + A[0] + A[i+1:] if not i == 0 else A
            combinations.append(currString)
        ans = '0'
        for s in combinations:
            newComb = self.solve(s[1:], B-1) if s != A else self.solve(s[1:], B)
            ans =  max(ans, s[0] + newComb)
        return ans
 *
 *
// Scala:
 * class Solution {
    def swap(s: String, i: Int, j: Int): String = {
    val cs = s.toCharArray
        val swp = cs(i)
        cs(i) = cs(j)
        cs(j) = swp
        new String(cs)
    }

    def solve(A: String, B: Int): String = {
        var maxString = A
        def loop2(swaps: Int, soFar: String): Unit = {
          var mutableStr = soFar
          if (swaps > 0)
            for {i <- 0 until soFar.length
                 j <- i + 1 until soFar.length
                 } {
              if (mutableStr.charAt(j) > mutableStr.charAt(i)) {
                mutableStr = swap(mutableStr, i, j)
                loop2(swaps - 1, mutableStr)
                mutableStr = swap(mutableStr, i, j)
              }
            } else
            if (mutableStr > maxString) maxString = mutableStr

        }

        loop2(B, A)
        maxString
    }
}
// GO
 * import "strings"
func solve(A string , B int )  (string) {
    maxSoFar := A
    a := strings.Split(A,"")
    recur(a,0,B,&maxSoFar)
    return maxSoFar
}

func swap(a []string, i, j int) []string {
    temp := a[i]
    a[i] = a[j]
    a[j] = temp
    return a
}

func compStringArr(a []string, b string) bool {
    temp := ""
    for _,v := range a{
        temp +=v
    }
    return temp > b
}

func recur(a []string, curn int, count int, maxSoFar *string) {
    if curn == len(a) || count == 0 {
        return
    }
    //findMaxChar
    maxChar := a[curn]
    for i:= curn+1 ; i< len(a);i ++ {
        if a[i] > maxChar {
            maxChar = a[i]
        }
    }
    //if MaxChar is same as curn, move on to next index
    if maxChar == a[curn] {
        recur(a, curn+1, count, maxSoFar)
    } else {
        //check if MaxChar at more than one place, recurse further with every possible swap
        for i := curn+1 ; i < len(a) ; i++ {
            if a[i] == maxChar {
                //if maxChar swap
                a = swap(a, curn, i)
                //compare to maxSoFar and save
                if  compStringArr(a, *maxSoFar) {
                    temp := ""
                    for _,v := range a{
                        temp +=v
                    }
                    *maxSoFar = temp
                }
                //recur by decrementing remaingng swaps(count)
                recur(a, curn+1, count-1, maxSoFar)
                //swap back in place, to try other possible swap
                a = swap(a, i, curn)
            }
        }
    }
}
 *
 */
