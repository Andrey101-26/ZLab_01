"""Ядро калькулятора"""

from toolkit import CalculatorError
from toolkit.tokenize import token
from toolkit.validate import val


def pri(w: str) -> int:
    """Определяет приоритет оператора"""
    if w in "*/":
        return 2
    else:
        return 1

def rpn(w: list) -> list:
    """Переводит токены в RPN"""
    r=[]
    s=[]
    for i in w:
        if i in "+-*/":
            while s and pri(s[-1]) >= pri(i):
                r.append(s.pop())
            s.append(i)
        else:
            r.append(i)
    while s:
        r.append((s.pop()))
    return r

def calc(w: list) -> float:
    """Считает RPN"""
    s=[]
    for i in w:
        if i in "+-*/":
            b=s.pop()
            a=s.pop()
            if i=="+":
                s.append(a+b)
            elif i=="-":
                s.append(a-b)
            elif i=="*":
                s.append(a*b)
            elif i=="/":
                if b==0:
                    raise CalculatorError("Деление на ноль")
                s.append(a/b)
        else:
            s.append(float(i))
    return s[0]

def exp(w: str) -> float:
    """Главная функция"""
    a=token(w)
    val(a)
    a=rpn(a)
    return calc(a)
