//============================================================================
// Name        : spiralOrderMat.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;
/*
Problem Description
Given a matrix of M * N elements (M rows, N columns), return all elements of the matrix in spiral order.
Problem Constraints
1 <= M, N <= 1000
Input Format
The first argument is a matrix A.
Output Format
Return an array of integers representing all elements of the matrix in spiral order.
Example Input
A =
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
Example Output
[1, 2, 3, 6, 9, 8, 7, 4, 5]
*/

//int main() {
	// cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	// return 0;
		// vector<int> Solution::spiralOrder(const vector<vector<int> > &A) {
	vector<int> spiralOrder(const vector<vector<int> > &A) {
	    std::vector<int> ans;
	    int m = A.size();
	    int n = A[0].size();
	    if (m == 0 || n == 0) {
	        return ans;
	    }

	    int low = 0;
	    int high = m - 1;
	    int left = 0;
	    int right = n - 1;

	    while (low <= high && left <= right) {
	        for (int i = left; i <= right; ++i) {
	        	ans.push_back(A[low][i]);
	        }
	        low++;

	        for (int i = low; i <= high; ++i) {
	        	ans.push_back(A[i][right]);
	        }
	        right--;

	        if (low <= high) {
	            for (int i = right; i >= left; --i) {
	            	ans.push_back(A[high][i]);
	            }
	            high--;
	        }

	        if (left <= right) {
	            for (int i = high; i >= low; --i) {
	            	ans.push_back(A[i][left]);
	            }
	            left++;
	        }
	    }

	    return ans;
	}
//}

/* Editorial
 *
vector<int> Solution::spiralOrder(const vector<vector<int> > &A) {
	vector<int> result;
	int r=A.size(), c=A[0].size();
	int r_beg=0,r_end=r,c_beg=0,c_end=c;
    while(r_beg<r_end && c_beg<c_end){
        for(int i=c_beg;i<c_end;i++)
            result.push_back(A[r_beg][i]);
        for(int i=r_beg+1;i<r_end;i++)
            result.push_back(A[i][c_end-1]);
        for(int i=c_end-2;i>=c_beg && (r_end-1-r_beg)>0;i--)
            result.push_back(A[r_end-1][i]);
        for(int i=r_end-2;i>r_beg && (c_end-1-c_beg)>0;i--)
            result.push_back(A[i][c_beg]);
        r_beg++;r_end--;
        c_beg++;c_end--;
    }
	return result;
}
 *
 */

/*
Scala:
class Solution {
    	def spiralOrder(A: Array[Array[Int]]): Array[Int]  = {
			var n_l = 0;
			var s_l = A.size - 1;
			var w_l = 0;
			var e_l = A(0).size - 1;
			var index = 0;
			val ret = new Array[Int](A.size * A(0).size);
			while ( n_l <= s_l && w_l <= e_l ) {
				for ( current_c <- w_l to e_l ) {
					ret(index) = A(n_l)(current_c);
					index+=1;
				}
				n_l = n_l + 1;
				for ( current_l <- n_l to s_l ) {
					ret(index) = A(current_l)(e_l);
					index+=1;
				}
				e_l = e_l - 1;
				if (n_l <= s_l) {
					for ( current_c <- e_l to w_l by -1) {
						ret(index) = A(s_l)(current_c);
						index+=1;
					}
					s_l = s_l - 1;
					if (w_l <= e_l) {
						for ( current_l <- s_l to n_l by -1) {
							ret(index) = A(current_l)(w_l);
							index+=1;
						}
						w_l = w_l + 1;
					}
				}
			}
			return ret;
	}
}

 */

/*
GO:
func spiralOrder(A [][]int) []int {
    var spiral []int
    nRows := len(A)
    if nRows == 0 {
        return spiral
    }

    nCols := len(A[0])
    rowStart, rowEnd := 0, nRows-1
    colStart, colEnd := 0, nCols-1
    dir := 0
    for rowStart <= rowEnd && colStart <= colEnd {
        switch dir {
        case 0:
            for c := colStart; c <= colEnd; c++ {
                spiral = append(spiral, A[rowStart][c])
            }
            rowStart++
        case 1:
            for r := rowStart; r <= rowEnd; r++ {
                spiral = append(spiral, A[r][colEnd])
            }
            colEnd--
        case 2:
            for c := colEnd; c >= colStart; c-- {
                spiral = append(spiral, A[rowEnd][c])
            }
            rowEnd--
        case 3:
            for r := rowEnd; r >= rowStart; r-- {
                spiral = append(spiral, A[r][colStart])
            }
            colStart++
        }

        dir = (dir + 1) % 4
    }

    return spiral
}
 */
