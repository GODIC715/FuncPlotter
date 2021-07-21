from TextToFunc import *

def test_prepString() -> str:
    assert prepString("sin(x)") == "sin(x)"
    assert prepString("x +         this IS J   UsT a Test") == "x+thisisjustatest"
    assert prepString("") == ""
    assert prepString(124) == "124"
