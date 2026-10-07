"""Валидация последовательности токенов."""

from toolkit import CalculatorError


def val(w: list) -> None:
    """Проверяет порядок"""
    for i in range(len(w)):
        if i%2==0:
            if w[i] in "+-*/":
                raise CalculatorError("Ошибка ввода оператора")
        else:
            if w[i] not in "+-*/":
                raise CalculatorError("Ошибка ввода числа")
    if len(w)==0:
        raise CalculatorError("Пустое выражение")
    if len(w)%2==0:
        raise CalculatorError("Неполное выражение")

