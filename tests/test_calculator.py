"""Тесты для ядра калькулятора."""
import pytest

from toolkit import CalculatorError
from toolkit.calculator import exp


def test_base_calc_1():
    assert exp("2+3")==5.0

def test_base_calc_2():
    assert exp("2+3*4") == 14.0

def test_base_calc_3():
    assert exp("10/4")==2.5

def test_base_calc_4():
    assert exp("10-3")==7.0

def test_base_calc_5():
    assert exp("2*3")==6.0

def test_base_calc_6():
    assert exp("-2*-3")==6.0

def test_nbase_calc_7():
    with pytest.raises(CalculatorError):
        exp("")

def test_nbase_calc_8():
    with pytest.raises(CalculatorError):
        exp("2 * * 3")

def test_abc_calc_9():
    with pytest.raises(CalculatorError):
        exp("2 + a")

def test_del_0_calc_10():
    with pytest.raises(CalculatorError):
        exp("1/0")
