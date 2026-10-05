from src.toolkit import CalculatorError


def token(w):
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
            else:
                if g != "":
                    a.append(g)
                a.append(b)
                g=""
                k=0
    if g != "":
        a.append(g)
    return a
def val(w):
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
def pri(w):
    if w in "*/":
        return 2
    else:
        return 1
def rpn(w):
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
def calc(w):
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
                s.append(a/b)
        else:
            s.append(float(i))
    return s[0]
def exp(w):
    a=token(w)
    val(a)
    a=rpn(a)
    return calc(a)