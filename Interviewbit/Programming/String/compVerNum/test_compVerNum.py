# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 15:47:05 2026

@author: USER
"""

import compVerNum
import pytest

def test_compareVersion():
    assert compVerNum.compareVersion("0.1", "1.1") == -1
    assert compVerNum.compareVersion("1.1", "0.1") == 1
    assert compVerNum.compareVersion("1.13.4", "1.13") == 1
    assert compVerNum.compareVersion("1.13.4", "1.2") == 1
    assert compVerNum.compareVersion("1.13.4", "1.1") == 1
    assert compVerNum.compareVersion("1.13.4", "0.1") == 1
    assert compVerNum.compareVersion("1.13", "1.13.4") == -1
    assert compVerNum.compareVersion("1.2", "1.13.4") == -1
    assert compVerNum.compareVersion("1.1", "1.13.4") == -1
    assert compVerNum.compareVersion("0.1", "1.13.4") == -1
    assert compVerNum.compareVersion("1.13.4.0", "1.13.4") == 0
    assert compVerNum.compareVersion("1.13.4.0", "1.13.4.0.0.0") == 0