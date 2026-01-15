# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 20:17:20 2026

@author: USER
"""

import primeNum
import pytest

def test_sieve():
    assert primeNum.sieve(0) == []
    assert primeNum.sieve(1) == []
    assert primeNum.sieve(2) == [2]
    assert primeNum.sieve(3) == [2, 3]
    assert primeNum.sieve(4) == [2, 3]
    assert primeNum.sieve(7) == [2,3,5,7]
    assert primeNum.sieve(10) == [2,3,5,7]
    assert primeNum.sieve(11) == [2,3,5,7,11]
    