# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 20:10:06 2026

@author: USER
"""

import lengthLastWord
import pytest

def test_lengthLastWord():
    assert lengthLastWord.lengthOfLastWord(" hello world ") == 5
    assert lengthLastWord.lengthOfLastWord("InterviewBit") == 12
    assert lengthLastWord.lengthOfLastWord("         ") == 0
