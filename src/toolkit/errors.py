"""Доменные ошибки toolkit."""


class ToolkitError(Exception):
    """Базовая ошибка приложения."""


class CalculatorError(ToolkitError):
    """Ошибка вычисления вырожения."""


class ConverterError(ToolkitError):
    """Ошибка конвертации велечин."""
