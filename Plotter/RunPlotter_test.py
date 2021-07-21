from PySide2 import QtCore
from RunPlotter import *
import pytest

@pytest.fixture
def window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    return window

# def test_bad_functionInput(qtbot, window):
#     qtbot.keyClicks(window.functionInput,"Some String that's bound to fail")
#     qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
#     assert window.testingVar == "somestringthat is not valid to use in math expression"


# def test_bad_functionInput2(qtbot, window):
#     qtbot.keyClicks(window.functionInput,"son(x)")
#     qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
#     assert window.testingVar == "som is not valid to use in math expression"

# def test_bad_functionInput3(qtbot, window):
#     qtbot.keyClicks(window.functionInput,"sin()")
#     qtbot.mouseClick(window.plotButton, QtCore.Qt.LeftButton)
#     assert window.testingVar == "sin is not valid to use in math expression"
