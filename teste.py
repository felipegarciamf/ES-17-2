import pytest
from principal import somar
from principal import sub


def test_somar():
    """ docstring for test somar"""
    assert somar(2, 3)==5

def test_sub():
    """ docstring for test subtrair """
    assert sub(2,2)==0

def test_mult():
    """ docstring for test mult """
    assert sub(2,3)==6
