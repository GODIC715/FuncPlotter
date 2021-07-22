from PySide2 import QtCore
from RunPlotter import *
import pytest

@pytest.fixture
def window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    return window

def test_bad_functionInput(qtbot, window):
    qtbot.keyClicks(window.functionInput,"Some String that's bound to fail")
    qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
    assert window.testingVar == "somestringthat is not valid to use in math expression"

def test_bad_functionInput2(qtbot, window):
    qtbot.keyClicks(window.functionInput,"son(x)")
    qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
    assert window.testingVar == "son is not valid to use in math expression"

def test_bad_functionInput3(qtbot, window):
    qtbot.keyClicks(window.functionInput,"sin()")
    qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
    assert window.testingVar == "You probably forgot to provide an argument somewhere. Check for 'sin()' for example"

def test_bad_functionInput4(qtbot, window):
    qtbot.keyClicks(window.functionInput,"sin(x")
    qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
    assert window.testingVar == "You probably forgot to close a bracket or provide a second number somewhere. Check for 'sin(x' or '5^' for example"

def test_evil_func(qtbot, window):
    qtbot.keyClicks(window.functionInput,"__import__('os').system('ls')")
    qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
    assert window.testingVar == "__import__ is not valid to use in math expression"

def test_evil_func2(qtbot, window):
    qtbot.keyClicks(window.functionInput,"eval('print(1+2)')")
    qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
    assert window.testingVar == "eval is not valid to use in math expression"

def test_lower_bound_equal_or_higher(qtbot,window):
    qtbot.keyClicks(window.functionInput,"sin(x)")
    window.lowerLimitSpin.setValue(10)
    window.upperLimitSpin.setValue(10)
    qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
    assert window.testingVar == "Lower bound must be explicitly lower than the upper bound"
    
    window.lowerLimitSpin.setValue(110)
    window.upperLimitSpin.setValue(10)
    qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
    assert window.testingVar == "Lower bound must be explicitly lower than the upper bound"

    # window.lowerLimitSpin.setValue(0)

def test_good_func(qtbot, window):
    qtbot.keyClicks(window.functionInput,"sin(x)")
    qtbot.mouseClick(window.plotButton,QtCore.Qt.LeftButton)
    assert window.testingVar == "Plotted successfully"

def test_good_func2(qtbot, window):
    qtbot.keyClicks(window.functionInput,"5")
    qtbot.mouseClick(window.plotButton,QtCore.Qt.LeftButton)
    assert window.testingVar == "Plotted successfully"