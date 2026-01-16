# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 21:35:46 2026

@author: USER
"""

import addWithoutSum
import pytest

def test_addNumbers():
    assert addWithoutSum.addNumbers(3, 10) == 13
    assert addWithoutSum.addNumbers(6, 1) == 7
    assert addWithoutSum.addNumbers(452887384, 989233850) == 1442121234
