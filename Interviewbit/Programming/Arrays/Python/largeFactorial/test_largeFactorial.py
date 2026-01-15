# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 23:06:27 2026

@author: USER
"""

import largeFactorial
import pytest

def test_sieve():
    assert largeFactorial.solve(2) == "2"
    assert largeFactorial.solve(3) == "6"

    