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