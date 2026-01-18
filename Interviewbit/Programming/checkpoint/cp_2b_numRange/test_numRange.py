# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 19:15:14 2026

@author: USER
"""

import numRange
import pytest

def test_numRange():
    A = [10, 5, 1, 0, 2]
    B, C = (6, 8)
    assert numRange.numRange(A, B, C) == 3
    A = [10, 5, 1, 0, 0, 2]
    B, C = (6, 8)
    assert numRange.numRange(A, B, C) == 4
    A = [10, 5, 1, 0, 0, 1, 2]
    B, C = (6, 8)
    assert numRange.numRange(A, B, C) == 4
    A = [10, 5, 1, 0, 0, 1, 2]
    B, C = (6, 9)
    assert numRange.numRange(A, B, C) == 5
    
