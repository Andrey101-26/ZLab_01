"""Тесты для ядра калькулятора."""
import pytest
from toolkit import CalculatorError
from toolkit.calculator import exp
def test_1():
    assert exp("2+3")==5.0
def test_2():
    assert exp("2+3*4") == 14.0
def test_3():
    assert exp("10/4")==2.5
def test_4():
    assert exp("10-3")==7.0
def test_5():
    assert exp("2*3")==6.0
def test_6():
    assert exp("-2*-3")==6.0
def test_7():
    with pytest.raises(CalculatorError):
        exp("")
def test_8():
    with pytest.raises(CalculatorError):
        exp("2 * * 3")
def test_9():
    with pytest.raises(CalculatorError):
        exp("2 + a")
def test_10():
    with pytest.raises(CalculatorError):
        exp("1/0")