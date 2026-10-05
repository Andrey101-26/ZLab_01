"""Конвертер величин."""
import json
import os

from toolkit.errors import ConverterError

cf=os.path.join(os.path.dirname(__file__),"units.json")
with open(cf,encoding="utf-8") as fh:
    units=json.load(fh)
def base(v,g,u):
    return v*units[g][u]
def unbase(v,g,u):
    return v/units[g][u]
def group(u):
    for a in units:
        if u in units[a]:
            return a
    else:
        return None
def tc(v,u):
    if u=="c":
        t=v
    if u=="f":
        t=((v-32)*5/9)
    if u=="k":
        t=(v-273.15)
    if t<(-273.15):
        raise ConverterError("Невозможная температура")
    return t
def fc(v,u):
    if u=="c":
        return v
    if u=="f":
        return (v*9/5)+32
    if u=="k":
        return v+273.15
def conv(v,n,k):
    a=group(n)
    b=group(k)
    if a!=b:
        raise ConverterError("Несовместимые единицы")
    if a=="temp":
        return fc(tc(v,n),k)
    else:
        return unbase(base(v,a,n),b,k)
