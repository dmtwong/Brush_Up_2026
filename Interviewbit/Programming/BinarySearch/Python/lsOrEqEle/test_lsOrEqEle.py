# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 22:05:50 2026

@author: USER
"""

import lsOrEqEle
import pytest

def test_solve():
    A = [1, 3, 4, 4, 6]
    B = 4
    assert lsOrEqEle.solve(A, B) == 4
    A = [1, 2, 5, 5]
    B = 3 # 2    
    assert lsOrEqEle.solve(A, B) == 2
    A = [ 1, 6, 9, 13, 15, 18, 20, 25, 29, 32, 35, 46 ]
    B = 28 
    assert lsOrEqEle.solve(A, B) == 8
