"""Токенизация выражений"""

from toolkit import CalculatorError


def token(w: str) -> list:
    """Разбивает строку на токены"""
    a=[]
    g=""
    k = 0
    for b in w:
        if b==" ":
            continue
        if b in "0123456789.":
            g = g + b
            k=1
        else:
            if b=="-" and k==0:
                g="-"+g
            elif b=="+" and k==0:
                continue
            elif b in "+-*/":
                if g != "":
                    a.append(g)
                a.append(b)
                g=""
                k=0
            else:
                raise CalculatorError("Недопустимый символ"+" "+b)
    if g != "":
        a.append(g)
    return a
