"""Доменные ошибки toolkit."""


class ToolkitError(Exception):
    """Базовая ошибка приложения."""


class CalculatorError(ToolkitError):
    """Ошибка вычисления выражения."""


class ConverterError(ToolkitError):
    """Ошибка конвертации величин."""
