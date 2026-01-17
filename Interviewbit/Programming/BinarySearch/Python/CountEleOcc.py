# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 21:26:10 2026

@author: USER
"""

'''
Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0
**Example : **
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2.
PROBLEM APPROACH :
For complete solution, look at the hint.
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def findCount(self, A, B):
'''
def findCount(A, B):
    # return A.count(B) # works but O(n)
    def bS(A, B, low, high):
        if low == high:
            if A[low] == B:
                # print(low)
                return low
        mid = (low + high) // 2
        if A[mid] == B:
            # print(mid)
            return mid
        elif A[mid] > B:
            if low != mid:
                return bS(A, B, low, mid - 1)
            else: 
                return 0
        else:
            return bS(A, B, mid + 1, high)
    
    n_A = len(A)
    if n_A == 0:
        return 0
    else:
        ix = bS(A, B, 0, n_A - 1)
        if A[ix] != B:
            return 0
        count = 1
    # print(ix, count)
    ix_back = ix
    while ix != 0:
        ix -= 1
        if A[ix] == B:
            count += 1
        else:
            break
    # print(count, 'here')
    while ix_back != (n_A - 1):
        ix_back += 1
        if A[ix_back] == B:
            count += 1
        else:
            break
    return count
      # A = [5, 7, 7, 8, 8, 10]
      # B = 8  
# findCount(A, B)  

# Scala:
'''
class Solution {
    
    var array : Array[Int] = Array[Int]()

    def findCount(A: Array[Int], B: Int): Int  = {
        array = A
        val position = binarySearch(B)
        if (position == -1) {
            0
        }
        else {
            var count = 1
            var index = position + 1
            while (index < array.length && array(index)== B) {
                count += 1
                index += 1
            }
            index = position - 1
            while (index >= 0 && array(index)== B) {
                count += 1
                index -= 1
            }
            count
        }
    }
    
    def binarySearch(elt : Int) : Int = {
		var start = 0
				var end = array.length - 1
				while (start <= end) {
					val mid = (start + end) / 2;
					val eltMid = array(mid);
					if (eltMid==elt) {
						return mid
					}
					else {
						if (elt > eltMid) {
							start = mid + 1;
						}
						else {
							end = mid - 1
						}
					}
				}
		-1
}
}
'''

# C++
'''
int Solution::findCount(const vector<int> &A, int B) {
    int st = lower_bound(A.begin(), A.end(), B)-A.begin();
    int ed = upper_bound(A.begin(), A.end(), B)-A.begin();
    return ed-st;
}
'''

# GO
'''
/**
 * @input A : Integer array
 * @input B : Integer
 *
 * @Output Integer
 */
func findCount(numbers []int , number int) (int) {
	idx := binarySearch(numbers, number, 0, len(numbers) - 1)
	if idx == - 1 {
		return 0
	}
	
	i := idx - 1
	count := 1
	for i >= 0 && numbers[i] == number {
		count++
		i--
	}
	
	i = idx + 1
	for i < len(numbers) && numbers[i] == number {
		count++
		i++
	}
	return count
}

func binarySearch(numbers []int, number, left, right int) int {
	
	if left <= right {
		mid := left + ((right - left) / 2)
		if numbers[mid] == number {
			return mid
		} else if numbers[mid] > number {
			return binarySearch(numbers, number, left, mid - 1)
		} else {
			return binarySearch(numbers, number, mid + 1, right)
		}
	}
	
	return -1
}

'''