"""CLI toolkit."""
import argparse
import sys

from toolkit.calculator import exp
from toolkit.converter import conv
from toolkit.errors import CalculatorError, ConverterError


def main() -> int:
    """Разбирает аргументы командной строки и вызывает ядро"""
    a=argparse.ArgumentParser(prog="toolkit")
    sub= a.add_subparsers(dest="command",required = True)
    calc_parser = sub.add_parser("calc",help="калькуляьтор")
    calc_parser.add_argument("expression", help="выражение для вычисления")
    conv_parser=sub.add_parser("convert", help="конвертер")
    conv_parser.add_argument("v",help="значение")
    conv_parser.add_argument("--from",dest="f",help="из чего")
    conv_parser.add_argument("--to",dest="t", help="во что")
    b=a.parse_args()
    try:
        if b.command == "calc":
            print(exp(b.expression))
        elif b.command == "convert":
            print(conv(float(b.v), b.f, b.t))
    except (CalculatorError, ConverterError) as e:
        print("error:",e,file=sys.stderr)
        return 2
    return 0
sys.exit(main())
