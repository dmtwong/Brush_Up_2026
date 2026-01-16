# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 22:45:19 2026

@author: USER
"""
import merge2sortedList
import pytest

def test_merge():
    A, B = [1, 5, 8], [6, 9]
    assert merge2sortedList.merge(A, B) == [1, 5, 6, 8, 9]
    A, B = [], []
    assert merge2sortedList.merge(A, B) == []
    A, B = [], [3]
    assert merge2sortedList.merge(A, B) == [3]
    A, B = [3], []
    assert merge2sortedList.merge(A, B) == [3]
