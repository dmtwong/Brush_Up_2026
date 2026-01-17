# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 22:55:42 2026

@author: USER
"""

import matMedian
import pytest

def test_findMedian():
    A = [   [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]   ] 
    assert matMedian.findMedian(A) == 5
    A = [   [5, 17, 100]    ]
    assert matMedian.findMedian(A) == 17
