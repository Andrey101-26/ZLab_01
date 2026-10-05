"""Пакет toolkit — калькулятор и конвертер."""
from toolkit.converter import conv
from toolkit.errors import CalculatorError, ConverterError, ToolkitError

__all__ = ["conv", "ToolkitError", "CalculatorError", "ConverterError"]
