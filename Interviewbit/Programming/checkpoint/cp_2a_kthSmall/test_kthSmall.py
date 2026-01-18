# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 18:25:22 2026

@author: USER
"""

import kthSmall
import pytest

def test_findMedian():
    A = [2, 1, 4, 3, 2]
    B = 3
    assert kthSmall.kthsmallest(A, B) == 2
    A = [1, 2]
    B = 2
    assert kthSmall.kthsmallest(A, B) == 2
    A = [ 8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
    B = 9
    assert kthSmall.kthsmallest(A, B) == 17
    A = [ 74, 90, 85, 58, 69, 77, 90, 85, 18, 36 ]
    B = 1
    assert kthSmall.kthsmallest(A, B) == 18