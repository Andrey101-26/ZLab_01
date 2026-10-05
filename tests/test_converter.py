"""Тесты для конвертера"""
import pytest

from toolkit import ConverterError
from toolkit.converter import conv


def test_1():
    assert conv(1000, "mm", "m") == 1.0
def test_2():
    assert conv(1.5, "kg", "g") == 1500.0
def test_3():
    assert conv(0, "c", "f") == 32.0
def test_4():
    assert conv(-273.15, "c", "k") ==pytest.approx(0.0, abs=1e-9)
def test_5():
    assert conv(1000, "MM", "M") == 1.0
def test_6():
    with pytest.raises(ConverterError):
        conv(-300, "c", "k")
def test_7():
    with pytest.raises(ConverterError):
        conv(1, "kg", "m")
def test_8():
    with pytest.raises(ConverterError):
        conv(1, "z", "m")
