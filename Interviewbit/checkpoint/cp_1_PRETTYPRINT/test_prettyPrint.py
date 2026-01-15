# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 17:50:47 2026

@author: USER
"""

import prettyPrint
import pytest

def test_prettyPrint():
    assert prettyPrint.prettyPrint(4) == [[4, 4, 4, 4, 4, 4, 4],
     [4, 3, 3, 3, 3, 3, 4],
     [4, 3, 2, 2, 2, 3, 4],
     [4, 3, 2, 1, 2, 3, 4],
     [4, 3, 2, 2, 2, 3, 4],
     [4, 3, 3, 3, 3, 3, 4],
     [4, 4, 4, 4, 4, 4, 4]]
    assert prettyPrint.prettyPrint(3) == [[3, 3, 3, 3, 3],
     [3, 2, 2, 2, 3],
     [3, 2, 1, 2, 3],
     [3, 2, 2, 2, 3],
     [3, 3, 3, 3, 3]]

    