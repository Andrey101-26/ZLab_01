"""Тесты для конвертера"""
import pytest

from toolkit import ConverterError
from toolkit.converter import conv


def test_base_conv_1():
    assert conv(1000, "mm", "m") == 1.0

def test_base_conv_2():
    assert conv(1.5, "kg", "g") == 1500.0

def test_base_conv_3():
    assert conv(0, "c", "f") == 32.0

def test_abs_zero_conv_4():
    assert conv(-273.15, "c", "k") ==pytest.approx(0.0, abs=1e-9)

def test_big_conv_5():
    assert conv(1000, "MM", "M") == 1.0

def test_bol_abs_zero_conv_6():
    with pytest.raises(ConverterError):
        conv(-300, "c", "k")

def test_base_error_conv_7():
    with pytest.raises(ConverterError):
        conv(1, "kg", "m")

def test_nbase_conv_8():
    with pytest.raises(ConverterError):
        conv(1, "z", "m")
