//============================================================================
// Name        : subarrayOddNum.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;


/*
Problem Description
Given an array of integers A and an integer B.
Find the total number of subarrays having exactly B odd numbers.
Problem Constraints
1 <= length of the array <= 105
1 <= A[i] <= 109
0 <= B <= A
Input Format
The first argument given is the integer array A.
The second argument given is integer B.
Output Format
Return the total number of subarrays having exactly B odd numbers.
Example Input
Input 1:
 A = [4, 3, 2, 3, 4]
 B = 2
Input 2:
 A = [5, 6, 7, 8, 9]
 B = 3
Example Output
Output 1:
 4
Output 2:
 1
Example Explanation
Explanation 1:
 The subarrays having exactly B odd numbers are:
 [4, 3, 2, 3], [4, 3, 2, 3, 4], [3, 2, 3], [3, 2, 3, 4]
Explanation 2:
 The subarrays having exactly B odd numbers is [5, 6, 7, 8, 9]
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}


*/

// int Solution::solve(vector<int> &A, int B) {
int solve(vector<int> &A, int B) {
    unordered_map<int, int> m;
    int result = 0;
    int n_A = A.size();
    vector<int> v(n_A); // even or odd
    for (int i = 0; i < n_A; i++){
        if (A[i] % 2 == 0){
            v[i] = 0;
        } else {
            v[i] = 1;
        }
    }

    int curr_odd_count = 0;
    for(int i=0; i < n_A; i++){
    	curr_odd_count += v[i];
        if (curr_odd_count==B) {
        	result++;
        }

        if (m.find(curr_odd_count - B) != m.end()) {
        	result += m[curr_odd_count-B];
        }
        m[curr_odd_count]++;
    }

    return result;
}

/*
 * int Solution::solve(vector<int> &A, int B) {
    int n = A.size();
    int count = 0;
    int prefix[n+1];
    memset(prefix, 0, sizeof(prefix));
    int odd = 0;
    // traverse in the array
    for (int i = 0; i < n; i++)
    {

      prefix[odd]++;
      // if array element is odd
      if (A[i] & 1)
          odd++;

      // when number of odd elements>=M
      if (odd >= B)
          count += prefix[odd - B];
    }
    return count;

}

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        count = 0
        prefix = [0] * (n+1)
        odd = 0;
    # traverse in the array
        for i in range(n):
            prefix[odd] += 1
        # if array element is odd
            if (A[i] & 1):
                odd+=1

        # when number of odd elements>=M
            if (odd >= B):
                count += prefix[odd - B]
        return count

func solve(A []int , B int )  (int) {
    if len(A) < B {
        return 0
    }
    odd := make([]int, 0, 10)

    for i, v := range A {
        if v%2 != 0 {
            odd = append(odd, i)
        }
    }

    fEven := 0
    lEven := -1
    i := 0
    sum := 0

    for i+B <= len(odd) {
        if B > 0 {
            if i == 0 {
                fEven = odd[i]
            } else {
                fEven = odd[i] - odd[i-1] - 1
            }

            if i+B == len(odd) {
                lEven = len(A) - odd[i+B-1] - 1
            } else {
                lEven = odd[i+B] - odd[i+B-1] - 1
            }
            sum += fEven + fEven*lEven + lEven + 1
        } else {
            if i == len(odd) {
                if len(odd) > 0 {
                    fEven = len(A) - 1 - odd[i-1]
                } else {
                    fEven = len(A)
                }
            } else if i == 0 {
                fEven = odd[i]
            } else {
                fEven = odd[i] - odd[i-1] - 1
            }
            sum += (fEven * (fEven + 1)) / 2
        }
        i++
    }
    return sum
}

 */
