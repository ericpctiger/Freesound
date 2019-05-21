#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from freesound.skeleton import fib

__author__ = "ericpctiger"
__copyright__ = "ericpctiger"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
