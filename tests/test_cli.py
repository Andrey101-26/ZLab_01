"""Тесты командной строки."""
import subprocess
import sys

def run_toolkit(*args):
    return subprocess.run(
        [sys.executable, "-m", "toolkit", *args],
        capture_output=True,
        text=True,
    )
def test_1():
    result = run_toolkit("calc", "2+3*4")
    assert result.returncode == 0
    assert result.stdout.strip() == "14.0"

def test_2():
    result = run_toolkit("convert", "1000", "--from", "mm", "--to", "m")
    assert result.returncode == 0
    assert result.stdout.strip() == "1.0"

def test_3():
    result = run_toolkit("calc", "1/0")
    assert result.returncode == 2
    assert "error" in result.stderr.lower()
    assert result.stdout == ""
