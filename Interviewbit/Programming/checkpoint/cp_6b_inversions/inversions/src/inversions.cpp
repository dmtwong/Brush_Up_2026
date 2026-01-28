//============================================================================
// Name        : inversions.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


/*
 * A : [ 84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60 ]
 * Expect: 290
Problem Description
Given an array A, count the number of inversions in the array.
Formally speaking, two elements A[i] and A[j] form an inversion if A[i] > A[j] and i < j
Example Input
A : [2, 4, 1, 3, 5]
Example Output
3
Example Explanation
A : [2, 4, 1, 3, 5]
Output : 3
as the 3 inversions are (2, 1), (4, 1), (4, 3).
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}

*/
#include <iostream>
#include <vector>
using namespace std;

int merge(vector<int> &A, int lo, int mid, int hi){
    vector <int> temp;
    int cnt = 0;
    int i = lo, j = mid+1;
    while(i<=mid && j<=hi){
        if(A[i]<=A[j]){
            temp.push_back(A[i]);
            i++;
        } else {
            temp.push_back(A[j]);
            j++;
            cnt += mid-i+1;
        }
    }

    while (j<=hi) {
        temp.push_back(A[j]);
        j++;
    }

    while (i<=mid) {
        temp.push_back(A[i]);
        i++;
    }
    for (int i = lo; i <= hi; ++i){
        A[i] = temp[i - lo];
    }

    return cnt;
}

int msort(vector<int> &A, int lo, int hi){
    int count = 0;
    if(lo>=hi){
        return count;
    }
    int mid = (lo+hi)/2;
    count += msort(A, lo, mid);
    count += msort(A, mid+1, hi);
    count += merge(A, lo, mid, hi);
    return count;
}
//int Solution::countInversions(vector<int> &A) {
int countInversions(vector<int> &A) {
    /*
    int i, count, n_A;
    n_A = A.size();
    count = 0;

    for (i = 0; i < n_A - 1; i++){
        if (A[i] > A[i+1]){
            count += 1;
        }
    }
    return count;
    */
    int count = msort(A,0,A.size()-1);
    return count;
}

/*
//int Solution::countInversions(vector<int> &A) {
int countInversions(vector<int> &A) {
	int count = msort(A);
	return count;

	int i, j, count, n_A;
	n_A = A.size();
	count = 0;
	if (n_A < 2){
        return count;
    }
	for (i = 0; i < n_A - 1; i++){
		j = i + 1;
		for (j; j < n_A; j++){
			if (A[i] > A[j]){
				count += 1;
			}
		}
	}
	return count;
}

	*/




/* contain bug
int merge(vector<int> &subA){
	vector <int> sorted_A;
    sorted_A.clear();
	int lo = 0;
	int hi = subA.size() - 1;
	int mid = (lo + hi) / 2;
	int cnt = 0;
	int i = lo;
	int j = mid + 1;
	while (i <= mid && j <= hi){
		if (subA[i] <= subA[j]){
			sorted_A.push_back(subA[i]);
			i++;
		} else {
			sorted_A.push_back(subA[j]);
			j++;
			cnt += mid-i+1; // if A[i] > A[j] then everything between i and mid as well, including i
		}
	}

	while (j <= hi) {
		sorted_A.push_back(subA[j]);
		j++;
	}

	while (i<=mid) {
		sorted_A.push_back(subA[i]);
		i++;
	}
	for (int i = lo; i <= hi; i++){
		subA[i] = sorted_A[i - lo];
	}

	return cnt;
}
int msort(vector<int> &subA, int lo, int hi){
	int count = 0;
	// int lo = 0;
	// int hi = subA.size() - 1;
	if(lo >= hi){
		return count;
	}
	int mid = (lo + hi)/2; // n = 7, mid = 3 n = 6, mid = 3 [0, 1, 2][3,4,5,6]
	// vector<int> lower = {subA.begin(), subA.begin() + mid - 1};
	count += msort(subA, lo, mid);
	// vector<int> larger = {subA.begin() + mid, subA.end()};
	count += msort(subA, mid + 1, hi);
	count += merge(subA);
	return count;
}



int Solution::countInversions(vector<int> &A) {
//int countInversions(vector<int> &A) {
    int result = msort(A, 0, A.size()- 1);
    return result;
}
 */
