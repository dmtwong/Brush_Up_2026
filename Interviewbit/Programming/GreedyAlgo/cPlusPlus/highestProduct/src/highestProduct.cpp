//============================================================================
// Name        : highestProduct.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


/*
 *
 * Problem Description
Given an array A, of N integers A.
Return the highest product possible by multiplying 3 numbers from the array.
NOTE: The solution will fit in a 32-bit signed integer.
Problem Constraints
3 <= N <= 5*105
Input Format
The first and the only argument is an integer array A.
Output Format
Return the highest possible product.
Example Input
Input 1:
A = [1, 2, 3, 4]
Input 2:
A = [0, -1, 3, 100, 70, 50]
Example Output
Output 1:
24
Output 1:
350000
Example Explanation
Explanation 1:
2 * 3 * 4 = 24
Explanation 2:
70 * 50 * 100 = 350000
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
*/

//int Solution::maxp3(vector<int> &A) {
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxp3(vector<int> &A) {
	sort(A.begin(), A.end());
	int ix_last = A.size() - 1;
	int last = A[ix_last];
	int res_1 = A[0] * A[1] * last;
	/* int res_2;
	return res_1;
	if (last < 0){
		return res_1 * A[2];
	}

	res_2 = A[ix_last - 1] * A[ix_last - 2] ;

	if (A[ix_last - 1] < 0){
		if (A[ix_last - 2] < 0){
			res_2 = A[ix_last - 1] * A[ix_last - 2];
		} else {
			return res_1 * A[2];
		}
	}
	*/
	int res_2 = A[ix_last - 2] * A[ix_last - 1] * last;
	int max_res = max(res_1, res_2);
	// max_res *= A[ix_last];
	return max_res;
	/*
	sort(A.begin(), A.end());
	int ix_last = A.size() - 1;
	int res_1 = A[0] * A[1];
	int res_2 = A[ix_last - 1] * A[ix_last - 2];
	int max_res = max(res_1, res_2);
	max_res *= max_res * A[ix_last];
	return max_res;
	*/

}
/*
 * Scala:
module.exports = {
    //param a : array of integers
    //return an integer
	maxp3 : function(a){
	    var compareNum = function(a,b){
	        a = parseInt(a); b = parseInt(b);
	        if(a < b) return -1;
	        if(a ===b ) return 0;
	        return 1;
	    }
	    var sorted = a.sort(compareNum);
	    var len = sorted.length;
	    var topThree = sorted[len - 1] * sorted[len - 2] * sorted[len - 3];
	    var topAndBotTwo = sorted[len - 1] * sorted[0] * sorted[1];
	    return Math.max(topThree, topAndBotTwo);
	}
};
 GO:
 import "math"
import "sort"
func maxp3(arr []int) (int) {
	sort.Ints(arr)
	lastIdx := len(arr) - 1
	return int(math.Max(float64(arr[lastIdx] * arr[0] * arr[1]), float64(arr[lastIdx - 2] * arr[lastIdx - 1] * arr[lastIdx])))
}
 */
