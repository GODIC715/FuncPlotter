from TextToFunc import *
import pytest

def test_prepString() -> str:
    assert prepString("sin(x)") == "sin(x)"
    assert prepString("x +         this IS J   UsT a Test") == "x+thisisjustatest"
    assert prepString("") == ""

@pytest.mark.xfail
def test_prepStringFail1():    
    assert prepString(124) == "124"

def test_evalFunction():
    mathFunction = evalFunction("sin(x)")
    assert mathFunction(5) == np.sin(5)

    mathFunction = evalFunction("someIllegalString")
    assert mathFunction("anything") == "NameError"

    mathFunction = evalFunction("cos(x)/sin(x)")
    assert mathFunction(5) == np.cos(5) / np.sin(5)

def test_bad_functionInput():
    assert checkFuncInput("Some String that's bound to fail") == "somestringthat is not valid to use in math expression"

def test_bad_functionInput2():
    assert checkFuncInput("son(x)") == "son is not valid to use in math expression"

def test_bad_functionInput3():
    mathFunction = evalFunction("sin()")
    assert mathFunction(5) == "TypeError"

def test_bad_functionInput4():
    mathFunction = evalFunction("sin(x")
    assert mathFunction(5) == "SyntaxError"

def test_evil_func():
    assert checkFuncInput("__import__('os').system('ls')") == "__import__ is not valid to use in math expression"

def test_evil_func2():
    assert checkFuncInput("eval('print(1+2)')") == "eval is not valid to use in math expression"