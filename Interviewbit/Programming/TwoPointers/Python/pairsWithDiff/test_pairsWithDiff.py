# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:05:29 2026

@author: USER
"""

import pairsWithDiff
import pytest

def test_solve():
    A, B = [5, 10, 3, 2, 50, 80], 78
    assert pairsWithDiff.solve(A, B) == 1
    A, B = [-10, 20], 30
    assert pairsWithDiff.solve(A, B) == 1
    A, B =  [ 478, 358, -38, -536, 705 ], 320
    assert pairsWithDiff.solve(A, B) == 0
    A, B = [ -259, -825, 459, 825, 221, 870, 626, 934, 205, 783, 850, 398 ], -42
    assert pairsWithDiff.solve(A, B) == 1