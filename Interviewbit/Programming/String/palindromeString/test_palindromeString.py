# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 19:14:09 2026

@author: USER
"""

import palindromeString
import pytest

def test_isPalindrome():
    assert palindromeString.isPalindrome("A man, a plan, a canal: Panama") == 1
    assert palindromeString.isPalindrome("race a car") == 0