# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 21:27:00 2026

@author: USER
"""

import CountEleOcc
import pytest

def test_findCount():
    A = [5, 7, 7, 8, 8, 10]
    B = 8
    assert CountEleOcc.findCount(A, B) == 2
    A = [ 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10 ]
    B = 1 # 2    
    assert CountEleOcc.findCount(A, B) == 2
    A = [ 4, 7, 7, 7, 8, 10, 10 ]
    B = 3 # 0
    assert CountEleOcc.findCount(A, B) == 0

