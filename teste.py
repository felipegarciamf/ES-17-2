import pytest
from principal import somar
from principal import sub


def test_somar():
    assert somar(2, 3)==5
