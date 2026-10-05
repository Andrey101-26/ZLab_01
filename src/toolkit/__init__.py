"""Пакет toolkit — калькулятор и конвертер."""
from src.toolkit.converter import conv
from src.toolkit.errors import CalculatorError, ConverterError, ToolkitError
__all__ = ["conv", "ToolkitError", "CalculatorError", "ConverterError"]